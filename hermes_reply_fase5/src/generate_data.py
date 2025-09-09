# src/generate_data.py
# Gera /data/sensors_readings.csv com 7 dias de leituras a cada 2 minutos para 6 máquinas e 4 variáveis.
# Reproduz a mesma lógica usada no notebook. Não requer internet.

import os, math, random
from datetime import datetime, timedelta
import numpy as np
import pandas as pd

np.random.seed(42)
random.seed(42)

BASE = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE, 'data')
os.makedirs(DATA_DIR, exist_ok=True)

def bounded(val, low, high):
    return max(low, min(high, val))

start = datetime(2025, 1, 1, 0, 0, 0)
step_minutes = 2
days = 7
steps = int(days * 24 * 60 / step_minutes)
machines = ['M1','M2','M3','M4','M5','M6']
lines = {'M1':'L1','M2':'L1','M3':'L2','M4':'L2','M5':'L3','M6':'L3'}
plant_id = 1

records = []
for mi, m in enumerate(machines, start=1):
    machine_id = mi
    line_id = int(lines[m][1])
    base_temp = np.random.uniform(25, 40) + mi
    base_vib  = np.random.uniform(0.3, 1.0) + mi*0.05
    base_press= np.random.uniform(30, 80) + mi*2.0
    base_curr = np.random.uniform(15, 30) + mi*1.5

    for t in range(steps):
        ts = start + timedelta(minutes=step_minutes*t)
        daily = math.sin(2*math.pi*(t*step_minutes)/(24*60))
        current_amp = bounded(base_curr + 10*daily + np.random.normal(0, 2.0), 0, 200)
        temperature_c = bounded(base_temp + 0.5*current_amp/10 + 15*daily + np.random.normal(0, 1.5), 15, 110)
        vibration_g = bounded(base_vib + 0.8*abs(daily) + np.random.normal(0, 0.25), 0.0, 20.0)
        pressure_bar = bounded(base_press + 5*daily + np.random.normal(0, 2.5), 0, 200)
        label = 'NORMAL'

        if np.random.rand() < 0.035:
            which = np.random.choice(['temp_curr','vib_only','press_only','mixed'])
            if which == 'temp_curr':
                current_amp = bounded(current_amp + np.random.uniform(40, 80), 0, 200)
                temperature_c = bounded(temperature_c + np.random.uniform(25, 50), 15, 110)
            elif which == 'vib_only':
                vibration_g = bounded(vibration_g + np.random.uniform(6, 12), 0.0, 20.0)
            elif which == 'press_only':
                pressure_bar = bounded(pressure_bar + np.random.uniform(50, 100), 0, 200)
            else:
                current_amp = bounded(current_amp + np.random.uniform(20, 60), 0, 200)
                pressure_bar = bounded(pressure_bar + np.random.uniform(30, 80), 0, 200)

        if (temperature_c > 95) or (current_amp > 150) or (vibration_g > 12) or (pressure_bar > 170):
            label = 'ANOMALO'

        records.append({
            'plant_id': plant_id,
            'line_id': line_id,
            'machine_id': machine_id,
            'sensor_id': machine_id,
            'sensor_type': 'snapshot',
            'reading_time': ts.isoformat(),
            'temperature_c': round(temperature_c, 3),
            'vibration_rms_g': round(vibration_g, 3),
            'pressure_bar': round(pressure_bar, 3),
            'current_amp': round(current_amp, 3),
            'label': label
        })

df = pd.DataFrame(records)
out_csv = os.path.join(DATA_DIR, 'sensors_readings.csv')
df.to_csv(out_csv, index=False)
print(f'Wrote: {out_csv}  rows={len(df)}')
