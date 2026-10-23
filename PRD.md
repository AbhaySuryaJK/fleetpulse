# FleetPulse — Connected Fleet Health Monitor

**Owner:** Abhay Keelara · **Timeline:** 12 weeks · **Effort:** ~5–6 hrs/week · **Budget:** $0 (free version)

---

## 1. Product Requirements Document (PRD)

### Problem
Small fleets of EVs or field robots usually rely on fixed-interval maintenance. That means parts get replaced too early (wasted cost) or fail before the next service (unplanned downtime). Fleet managers have little real-time visibility into asset health.

### Target user
**Fleet Operations Manager** responsible for 5–20 battery-powered assets such as delivery robots, campus EV carts, or e-scooters.

**Their needs:** know which asset is at risk *before* it fails, plan maintenance around operations, and justify maintenance spend to leadership.

### Goals and KPIs

| Goal | KPI | Target |
|---|---|---|
| Detect faults early | Anomaly detection recall | ≥ 80% on test data |
| Avoid false alarms | Precision | ≥ 70% |
| Real-time visibility | Sensor-to-dashboard latency | < 10 seconds |
| Business value | Simulated downtime reduction vs. scheduled maintenance | ≥ 20% |
| Project delivery | Schedule variance / budget variance | Within ±10% |

### Scope
**In scope (MVP):**
- 2–3 sensor nodes monitoring voltage, current, temperature, and vibration
- Cloud data logging
- Anomaly-detection model (start with thresholds, then simple ML)
- Ops dashboard with health status, alerts, and trends
- Cost-benefit analysis: predictive vs. scheduled maintenance

**Out of scope (future):** a real vehicle, mobile app, multi-tenant users, production-grade security.

### Functional requirements
1. Each node reports sensor readings every 1–5 seconds.
2. The system stores readings with timestamp and asset ID.
3. The dashboard shows every asset's status as Healthy, Warning, or Critical.
4. The system raises an alert when readings deviate from normal patterns.
5. The dashboard shows a 24-hour trend per asset.

### System architecture
```
[ESP32 + sensors] --Wi-Fi/MQTT--> [Cloud: Firebase or AWS IoT free tier]
                                          |
                                  [Python: anomaly model]
                                          |
                                  [Dashboard: Streamlit or Grafana]
```

### Minimal-cost build plan

**Tier 0 — $0 (start here):** Build the whole system in the free **Wokwi** online ESP32 simulator, which includes virtual temperature, accelerometer, and potentiometer sensors. Add a Python script that simulates a fleet of 10 assets. Everything else uses free tiers: Firebase or HiveMQ (free MQTT broker) for data, and Streamlit Community Cloud to host the dashboard as a **public link you can share on LinkedIn**.

**Tier 1 — about $10–15 (optional, for a real demo video):** one physical node.

| Item | Qty | Est. cost |
|---|---|---|
| ESP32 dev board | 1 | $5–8 |
| DS18B20 temperature sensor | 1 | $2–3 |
| MPU6050 accelerometer (vibration) | 1 | $2–3 |
| Resistors (voltage divider to read battery voltage via ESP32 ADC) | 2 | ~$0 |
| **Total** | | **~$10–15** |

**Save more:** ask at Northeastern makerspaces or labs, or classmates from ECE, whether you can borrow parts. Bring components from your undergrad kit if you have any.

One real node plus nine simulated ones still tells the full "fleet" story.

> **Safety note:** use AA packs or USB power. Avoid bare Li-ion cells unless you have a proper protection circuit.

> **Safety note:** use AA packs or a bench supply to simulate a "battery." Avoid bare Li-ion cells unless you have a proper protection circuit.

---

## 2. Milestones (free version · starts Wed, Oct 21, 2026)

Each week runs **Wednesday → Tuesday**. Every **Tuesday**, write a 1-paragraph status update (done / next / blockers) in `/docs/status.md`. This habit is real TPM practice and great interview material.

| Phase | Weeks | Dates | Deliverable |
|---|---|---|---|
| 1. Setup and planning | 1–2 | Oct 21 – Nov 3 | Node running, repo, PRD v2, Gantt, Kanban |
| 2. Data pipeline | 3–5 | Nov 4 – Nov 24 | Cloud link, 10-asset fleet simulator, dataset |
| 3. Dashboard and model | 6–9 | Nov 25 – Dec 22 | Dashboard v1, anomaly model, public dashboard |
| 4. Business case | 10–11 | Dec 23 – Jan 5 | Cost-benefit report, retrospective, case study |
| 5. Launch | 12 | Jan 6 – Jan 12 | Demo video, final post, resume bullet |

Weeks 6–8 are deliberately light (Thanksgiving and finals season). Winter break (weeks 9–11) is where you catch up.

---

## 3. Week-by-week plan

### Week 1 · Oct 21 – 27 · Get started (~5 hrs)
- [ ] **Wed (2 hrs):** run the MicroPython node in Wokwi; push it into WARNING/CRITICAL and screen-record it; create the `fleetpulse` GitHub repo with a README; upload `main.py` and `diagram.json`; pick your story (campus EV cart fleet or field robot fleet)
- [ ] **Thu–Fri (1 hr):** message 2–3 people (NU PM Club, classmates with industry experience, ops people on LinkedIn) asking for a 15-min chat on how fleet maintenance decisions are made
- [ ] **Weekend (1.5 hrs):** hold the chats; note 3–5 insights in `/docs/user-research.md`
- [ ] **Tue (30 min):** first status update

**Done when:** node runs, repo is live, at least one user chat is done.

### Week 2 · Oct 28 – Nov 3 · Plan like a PM (~5 hrs)
- [ ] Update the PRD with your user insights (PRD v2) and save it to `/docs`
- [ ] Build a Gantt chart for weeks 1–12 (GanttProject or Excel, both free)
- [ ] Set up a Kanban board in GitHub Projects: Backlog → This week → In progress → Done
- [ ] Review the risk register and add any new risks
- [ ] **Publish LinkedIn post 1** (kickoff) with your Wokwi video
- [ ] Status update

**Done when:** PRD v2, Gantt, and Kanban are in the repo and post 1 is live.

### Week 3 · Nov 4 – 10 · Connect to the cloud (~6 hrs)
- [ ] Add Wi-Fi to the Wokwi node (network `Wokwi-GUEST`)
- [ ] Publish readings to the free HiveMQ public MQTT broker using `umqtt.simple`
- [ ] On your laptop, write a Python subscriber (`paho-mqtt`) that receives the readings and saves them to a CSV
- [ ] Status update

**Done when:** readings from Wokwi appear in a CSV on your laptop in real time.

### Week 4 · Nov 11 – 17 · Build the fleet (~6 hrs)
- [ ] Write a Python fleet simulator for 9 more assets (EV-02 … EV-10) publishing to the same broker
- [ ] Give each asset realistic behavior: slow battery drain, heat under load, and random injected faults (overheating, deep discharge, loose mount = high vibration)
- [ ] Label each injected fault in the data (`fault: true/false`) so you can measure the model later
- [ ] **Publish LinkedIn post 2** (the PM side: PRD, KPIs, risk register, user insights)
- [ ] Status update

**Done when:** 10 assets stream data together and faults are labeled.

### Week 5 · Nov 18 – 24 · Build the dataset (~5 hrs)
- [ ] Run the simulator to generate several days of fleet data (you can speed up simulated time)
- [ ] Store it in SQLite or CSV files in the repo under `/data`
- [ ] Do a quick exploration in a Jupyter notebook: plot temperature, voltage, and vibration per asset
- [ ] Status update

**Done when:** a clean, labeled dataset and one notebook with charts are in the repo.

### Week 6 · Nov 25 – Dec 1 · Dashboard v1 (~3 hrs, Thanksgiving week)
- [ ] Build a Streamlit dashboard: fleet table with green/yellow/red status per asset, plus a trend chart for a selected asset
- [ ] **Publish LinkedIn post 3** (first data: a screenshot of the dashboard or charts)
- [ ] Status update

**Done when:** the dashboard runs locally and shows all 10 assets.

### Week 7 · Dec 2 – 8 · Anomaly detection (~4 hrs, finals prep)
- [ ] Baseline: your existing threshold rules. Measure precision and recall against the fault labels
- [ ] Model: Isolation Forest with scikit-learn. Measure precision and recall again
- [ ] Record both results in a small table; compare with your PRD targets (recall ≥ 80%, precision ≥ 70%)
- [ ] Status update

**Done when:** you can say "the model beat / didn't beat the rules, and here's why."

### Week 8 · Dec 9 – 15 · Buffer week (~1–2 hrs, finals)
- [ ] Only fix bugs and catch up on anything that slipped
- [ ] Status update. Note any schedule variance against your Gantt chart (a good EM talking point)

**Done when:** you're back on track, or the plan is updated to reflect reality.

### Week 9 · Dec 16 – 22 · Dashboard v2 and go public (~6 hrs)
- [ ] Add the model's predictions to the dashboard: alerts panel, "at-risk assets" list, fleet health score
- [ ] Make the dashboard replay the recorded dataset so it works without a live broker
- [ ] Deploy it free on Streamlit Community Cloud to get a public link
- [ ] **Publish LinkedIn post 4** (dashboard demo + public link)
- [ ] Status update

**Done when:** anyone can open your dashboard from a link.

### Week 10 · Dec 23 – 29 · Business case (~5 hrs)
- [ ] Simulate two strategies over 6 months: scheduled maintenance vs. predictive maintenance based on your model's alerts
- [ ] Compare downtime hours, number of failures, maintenance cost, and MTBF. State your cost assumptions clearly
- [ ] Write a 1–2 page business case in `/docs/business-case.md` with a recommendation
- [ ] Status update

**Done when:** you have one headline number, e.g. "predictive maintenance cut simulated downtime by X%."

### Week 11 · Dec 30 – Jan 5 · Retrospective and case study (~5 hrs)
- [ ] Retrospective: KPIs vs. targets, schedule and budget variance, what went well, what you'd change
- [ ] Polish the README into a case study: problem → users → approach → results → lessons, with screenshots and the dashboard link
- [ ] **Publish LinkedIn post 5** (business case result)
- [ ] Status update

**Done when:** a recruiter could understand the whole project from the README in 3 minutes.

### Week 12 · Jan 6 – 12 · Launch (~5 hrs)
- [ ] Record a 60–90 second demo video: problem, dashboard, a fault being caught, business result
- [ ] **Publish LinkedIn post 6** (wrap-up with video, GitHub, and dashboard links)
- [ ] Add the project to LinkedIn's Featured section and your resume (fill in the bullet below)
- [ ] Offer to present it at the NU Project Management Club
- [ ] Final status update

**Done when:** it's on your resume, LinkedIn, and GitHub, and you can pitch it in 60 seconds.

---

## 4. Risk register

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | Wokwi or free-tier tool limits | Low | Medium | Fall back to the Python simulator and local CSV storage |
| 2 | Coursework crunch (midterms) | High | High | Weeks 6–8 are planned light; week 8 is a buffer; catch up over winter break |
| 3 | Not enough real fault data | High | Medium | Inject faults (overheat, overload, loose mount) and generate synthetic data |
| 4 | Cloud free-tier limits | Low | Low | Reduce sampling rate or log locally to CSV |
| 5 | Scope creep | Medium | High | Anything not in MVP goes to a "v2" list |

---

## 5. LinkedIn "build in public" plan

Post roughly every 2 weeks (dates follow the week-by-week plan). A series gets more recruiter attention than a single post at the end.

| Post | When | Content |
|---|---|---|
| 1. The kickoff | Week 2 | Problem, what you're building, and why (EE + EM angle) |
| 2. The PM side | Week 4 | Your PRD, KPIs, or risk register as an image; what you learned from user interviews |
| 3. First data | Week 6 | Screenshot or short clip of live sensor data |
| 4. The dashboard | Week 9 | Dashboard demo with a public Streamlit link |
| 5. The business case | Week 11 | Cost-benefit result: "predictive maintenance cut simulated downtime by X%" |
| 6. Wrap-up | Week 12 | 60–90 sec demo video, lessons learned, GitHub link |

**Tips:** tag Northeastern and the NU Project Management Club, use hashtags like #ProjectManagement #IoT #PredictiveMaintenance #TPM, and keep visuals simple (one image or a short video per post).

### Draft post 1
> Most fleets still replace parts on a fixed schedule — too early wastes money, too late means breakdowns.
>
> For the next 12 weeks, I'm building **FleetPulse**: a low-cost IoT system that monitors battery, temperature, and vibration across a simulated EV fleet and predicts failures before they happen.
>
> As an ECE grad now pursuing an MS in Engineering Management at Northeastern, I'm running this like a real program — PRD, KPIs, risk register, and a business case — not just a tech demo.
>
> Budget: under $15. I'll share progress every two weeks. 🔋
>
> #ProjectManagement #IoT #PredictiveMaintenance #EngineeringManagement #Northeastern

---

## 6. Resume bullet (fill in once done)
> Led end-to-end development of an IoT predictive-maintenance system for a simulated EV fleet. Defined PRD and KPIs, delivered on a $__ budget in 12 weeks, and achieved __% fault-detection recall with an estimated __% reduction in downtime vs. scheduled maintenance.
