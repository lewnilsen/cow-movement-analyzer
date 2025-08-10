import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import warnings

# Calculates the distance between two GPS points in meters
def haversine_m(lat1, lon1, lat2, lon2):
    R = 6371000  # Earth radius in meters
    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))

    return R * c


# Cow movement GPS data
def simulate_gps_data(seed=42, num_cows=20, duration_minutes=1440, step_minutes=1, simulate_sampling_gaps=False):

    # Random seed
    if seed is not None:
        random.seed(seed)
        np.random.seed(seed)

    # Paddock area
    paddock = {
        "lat_min": -36.86511724320055,
        "lat_max": -36.86359792987984,
        "lon_min": 174.72546796914588,
        "lon_max": 174.72742061726046
    }

    # Timestamps for data points
    steps = duration_minutes // step_minutes
    start_time = datetime(2025, 1, 1, 6, 0)  # Start at 6 AM
    timestamps = []
    for i in range(steps):
        timestamps.append(start_time + timedelta(minutes=i * step_minutes))

    # List of cows
    cows = []
    for i in range(1, num_cows + 1):
        cows.append(f"Cow {i:02d}")

    # Random start points
    positions = {}
    for cow in cows:
        lat = np.random.uniform(paddock["lat_min"], paddock["lat_max"])
        lon = np.random.uniform(paddock["lon_min"], paddock["lon_max"])
        positions[cow] = (lat, lon)

    # Random night movements
    restlessness = {}
    for cow in cows:
        restlessness[cow] = np.random.uniform(0.0, 0.5)

    rows = []

    #filling data for each point
    for ts in timestamps:
        # Assign night flag
        is_night = False
        if ts.hour >= 20 or ts.hour < 5:
            is_night = True

        #Cow movement
        for cow in cows:
            prev_lat, prev_lon = positions[cow]

           #grazing & walking speeds
            if random.random() < 0.4:
                move_dist_m = np.random.uniform(0.1, 0.3) 
            else:
                move_dist_m = np.random.uniform(1.5, 5.0)

            # Different speed for night time to simulate sleep with some movement
            if is_night == True:
                if np.random.rand() < restlessness[cow]:
                    move_dist_m = np.random.uniform(3.0, 10.0)
                else:
                    move_dist_m = move_dist_m * 0.5

            #Adding random spikes to simulate bad data
            if random.random() < 0.005:
                move_dist_m = np.random.uniform(100.0, 200.0)

            #Move cows in a random direction inside paddock
            angle = np.random.uniform(0, 2 * np.pi)
            delta_lat = (move_dist_m * np.cos(angle)) / 111_000
            delta_lon = (move_dist_m * np.sin(angle)) / (111_000 * np.cos(np.radians(prev_lat)))
            lat = prev_lat + delta_lat
            lon = prev_lon + delta_lon
            lat = np.clip(lat, paddock["lat_min"], paddock["lat_max"])
            lon = np.clip(lon, paddock["lon_min"], paddock["lon_max"])

            # Calculate speed
            distance = haversine_m(prev_lat, prev_lon, lat, lon)
            speed_m_s = distance / 60

            # Determine grazing status
            if speed_m_s <= 0.06:
                is_grazing = True
            else:
                is_grazing = False

            #Add rows
            rows.append({
                "cow_id": cow,
                "timestamp": ts,
                "lat": lat,
                "lon": lon,
                "speed_m_s": speed_m_s,
                "is_grazing": is_grazing,
                "is_night": is_night
            })

            # Update cow's position
            positions[cow] = (lat, lon)

    # DataFrame
    df = pd.DataFrame(rows)

    #sampling gap for data validation showcase, dropping 1-3% of rows if enabled
    if simulate_sampling_gaps == True:

        def drop_random_rows(group):
            drop_frac = np.random.uniform(0.01, 0.03)
            group = group.sample(frac=1 - drop_frac, random_state=seed)
            group = group.sort_values("timestamp")
            return group
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=FutureWarning)
            df = df.groupby("cow_id", group_keys=False).apply(drop_random_rows)

        df = df.reset_index(drop=True)
        df = df.sort_values(["cow_id", "timestamp"])
        

    #Metadata
    meta = {
        "paddock": paddock,
        "seed": seed,
        "start_time": start_time.isoformat(),
        "step_minutes": step_minutes
    }

    return df, meta
