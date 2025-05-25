import requests
import pandas as pd
from pyswarm import pso

def get_latest_meeting_key(circuit_name):
    url = "https://api.openf1.org/v1/meetings"
    response = requests.get(url)
    if response.status_code != 200:
        return None

    df = pd.DataFrame(response.json())
    if df.empty:
        return None

    circuit_name = circuit_name.lower().strip()
    filtered = df[df['circuit_short_name'].str.lower().str.contains(circuit_name)]

    if filtered.empty:
        return None

    # Pick the meeting_key for the latest year available for this circuit
    latest_meeting = filtered.loc[filtered['year'].idxmax()]
    return latest_meeting['meeting_key']

def fetch_pit_data(meeting_key):
    url = f"https://api.openf1.org/v1/pit?meeting_key={meeting_key}"
    response = requests.get(url)
    if response.status_code != 200:
        return pd.DataFrame()

    try:
        return pd.DataFrame(response.json())
    except:
        return pd.DataFrame()

def simulate_race(lap1, lap2, tire_type, total_laps=70):
    base_lap_time = 90
    tire_penalty = [0, 2.5, 5]  # Soft, Medium, Hard
    pit_stop_penalty = 22

    tire_type = int(tire_type)
    lap1, lap2 = int(lap1), int(lap2)

    total_time = total_laps * (base_lap_time + tire_penalty[tire_type])
    if lap1 != lap2:
        total_time += 2 * pit_stop_penalty
    if abs(lap2 - lap1) < 10:
        total_time += 10
    else:
        total_time += pit_stop_penalty
    return total_time

def strategy_objective(x):
    return simulate_race(x[0], x[1], x[2])

def optimize_strategy():
    lb = [5, 10, 0]
    ub = [50, 65, 2]
    best, _ = pso(strategy_objective, lb, ub, swarmsize=20, maxiter=10)
    return best

def generate_strategy(meeting_key):
    pit_data = fetch_pit_data(meeting_key)
    if pit_data.empty:
        return "No pit data available for this meeting."

    strategy = optimize_strategy()
    lap1 = int(round(strategy[0]))
    lap2 = int(round(strategy[1]))
    tire_index = int(round(strategy[2]))
    tire_names = ['Soft', 'Medium', 'Hard']
    tire_name = tire_names[tire_index]

    if lap1 == lap2 or abs(lap1 - lap2) <= 5:
        return f"Recommended 1-stop strategy: Pit on lap {lap1} using {tire_name} tires."
    else:
        return f"Recommended 2-stop strategy: Pit on laps {lap1} and {lap2} using {tire_name} tires."
