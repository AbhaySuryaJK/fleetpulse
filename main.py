# FleetPulse - Node EV-01 (Wokwi, MicroPython on ESP32)
# Reads temperature, battery voltage, and vibration,
# then prints a health status as JSON every 2 seconds.

import json, math, time
from machine import Pin, ADC, I2C
import onewire, ds18x20

# ---------- Asset ----------
ASSET_ID = "EV-01"

# ---------- Thresholds (tune later from your PRD) ----------
TEMP_WARN, TEMP_CRIT = 45.0, 60.0   # deg C
VOLT_WARN, VOLT_CRIT = 10.5, 9.9    # volts (3S pack, 9.0-12.6 V)
VIB_WARN,  VIB_CRIT  = 2.0,  5.0    # m/s^2 above gravity

# ---------- Sensors ----------
# DS18B20 temperature on GPIO 4
ds = ds18x20.DS18X20(onewire.OneWire(Pin(4)))
roms = ds.scan()

# Potentiometer = simulated battery voltage on GPIO 34
adc = ADC(Pin(34))
adc.atten(ADC.ATTN_11DB)            # full 0-3.3 V range

# MPU6050 on I2C (SDA 21, SCL 22)
i2c = I2C(0, sda=Pin(21), scl=Pin(22))
MPU = 0x68
i2c.writeto_mem(MPU, 0x6B, b'\x00') # wake up sensor


def read_temp():
    ds.convert_temp()
    time.sleep_ms(750)
    return ds.read_temp(roms[0])


def read_voltage():
    raw = adc.read()                           # 0 - 4095
    return 9.0 + (raw / 4095) * (12.6 - 9.0)   # map to battery range


def to_signed(hi, lo):
    v = (hi << 8) | lo
    return v - 65536 if v > 32767 else v


def read_vibration():
    d = i2c.readfrom_mem(MPU, 0x3B, 6)
    ax, ay, az = (to_signed(d[i], d[i + 1]) / 16384 * 9.81 for i in (0, 2, 4))
    return abs(math.sqrt(ax * ax + ay * ay + az * az) - 9.81)  # remove gravity


def level(v, warn, crit, low_is_bad=False):
    if low_is_bad:
        return 2 if v <= crit else 1 if v <= warn else 0
    return 2 if v >= crit else 1 if v >= warn else 0


STATUS = ["HEALTHY", "WARNING", "CRITICAL"]
print(json.dumps({"info": "FleetPulse node started"}))

while True:
    temp = read_temp()
    volt = read_voltage()
    vib = read_vibration()

    worst = max(level(temp, TEMP_WARN, TEMP_CRIT),
                level(volt, VOLT_WARN, VOLT_CRIT, low_is_bad=True),
                level(vib, VIB_WARN, VIB_CRIT))

    print(json.dumps({
        "asset": ASSET_ID,
        "ms": time.ticks_ms(),
        "temp": round(temp, 1),
        "volt": round(volt, 2),
        "vib": round(vib, 2),
        "status": STATUS[worst],
    }))
    time.sleep(1.25)   # ~2 s per reading including temp conversion
