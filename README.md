﻿# Formula1_strategy
# 🏎️ F1 Pit Stop Strategy Optimizer

This project predicts an **optimal pit stop strategy** for a Formula 1 race based on a given circuit name using real-world data from the [OpenF1 API](https://openf1.org/). It's powered by **Particle Swarm Optimization (PSO)** to simulate and optimize race strategies. The frontend is a stylish HTML page with a racing background video, and the backend is powered by Python and Flask.

---

## 🚀 Features

- 🔎 Accepts **circuit name input** (e.g., `monza`, `suzuka`, `spa`) and returns a strategy.
- ⚙️ Optimizes using a **custom simulation model + PSO**.
- 🌐 Uses **live OpenF1 API** to fetch pit stop and meeting data.
- 🎨 Beautiful, minimal UI with background video and clean CSS.
- 📦 Ready for extension with weather, driver, or tire wear data.

---

## 📸 UI Preview

> ![Preview](cars.gif)  

---

## 🧠 How It Works

1. User enters a **circuit name**.
2. The backend uses [OpenF1 API](https://openf1.org/) to find the latest **meeting key**.
3. Pit stop data is fetched for that meeting.
4. A **race simulation** runs using various pit stop timings and tire types.
5. PSO is used to find the **best combination** of pit laps and tire type.
6. The strategy is returned on the same page.

---

## 🗂️ Project Structure

```bash
├── app.py              # Flask app to handle routing and logic
├── main.py             # Core simulation + optimization logic
├── templates/
│   └── index.html      # Beautifully styled input/output page
├── static/
│   └── cars.mp4        # Racing background video
├── requirements.txt    # Python dependencies
└── README.md
