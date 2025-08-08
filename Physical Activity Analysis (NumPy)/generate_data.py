import numpy as np

def activity_data(seed = 42):
    np.random.seed(42)
    steps_data = np.random.randint(2000, 15000, 30)
    calories_data = np.random.randint(1500, 3000, 30)
    pulse_data = np.random.randint(60, 120, 30)
    sleep_data = np.random.randint(4, 10, 30)
    full_activity_data = np.column_stack((steps_data, calories_data, pulse_data, sleep_data))
    return full_activity_data

