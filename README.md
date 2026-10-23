# 🔋 FleetPulse

**Predicting EV fleet failures before they happen.**

FleetPulse is a low-cost IoT system that monitors battery voltage, temperature, and vibration across a simulated EV fleet and flags faults early. It's run like a real program, with a PRD, KPIs, a risk register, and weekly status updates, as part of my MS in Engineering Management at Northeastern University.

| 🟢 Healthy | 🔴 Critical |
|---|---|
| ![Healthy node](docs/images/healthy.jpg) | ![Critical node](docs/images/critical.jpg) |
| 22 °C · 10.5 V · no vibration | 60.2 °C overheating + 9.0 V drained battery |

## How it works
1. **Sense:** ESP32 nodes read battery voltage, temperature, and vibration
2. **Stream:** data flows to the cloud over MQTT *(week 3)*
3. **Detect:** statistical and ML models flag anomalies *(week 7)*
4. **Decide:** a dashboard and business case comparing predictive vs. scheduled maintenance *(weeks 9–10)*

## Health status
| Status | Meaning |
|---|---|
| 🟢 HEALTHY | All readings normal |
| 🟡 WARNING | Temp ≥ 45 °C, battery ≤ 10.5 V, or vibration ≥ 2 m/s² |
| 🔴 CRITICAL | Temp ≥ 60 °C, battery ≤ 9.9 V, or vibration ≥ 5 m/s² |

## Run it yourself
1. Go to [wokwi.com](https://wokwi.com) and create a new **ESP32 → MicroPython** project
2. Paste `main.py` and `diagram.json` from this repo into the matching tabs
3. Press ▶ Play, then click the sensors or turn the knob to trigger faults

## Repo structure
```
main.py          # Sensor node firmware (MicroPython, ESP32)
diagram.json     # Wokwi circuit: ESP32 + DS18B20 + MPU6050 + potentiometer
docs/PRD.md      # Product requirements, KPIs, 12-week plan, risk register
docs/status.md   # Weekly status updates
```

## Tech stack
ESP32 · MicroPython · Wokwi simulator · *(coming: MQTT, Python, scikit-learn, Streamlit)*

## Progress
- **Week 1:** first sensor node (EV-01) running in simulation, detecting overheating and battery drain ✅

## Author
**Abhay Keelara**, MS Engineering Management, Northeastern University
