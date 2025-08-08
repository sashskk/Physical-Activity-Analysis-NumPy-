import numpy as np
from generate_data import activity_data
from analyze import (
    average_steps,
    lazy_days,
    high_pulse_day,
    most_sleep_time,
    labels,
    best_steps_ratio
)

data = activity_data()

print('Monthly statistics:')
print()
print(f'Average count of steps: {int(average_steps(data))}')
print(f'Lazy days (< 5000 steps): {len(lazy_days(data))}')
print(f'Max. heart rate: {high_pulse_day(data)[1]} (Day {high_pulse_day(data)[0]})')
print(f'The longest dream: {most_sleep_time(data)[1]}h. (Day {most_sleep_time(data)[0]})')
print()
print('Categories:')
print(f'Active days: {np.unique(labels(data), return_counts=True)[1][0]}')
print(f'Normal days: {np.unique(labels(data), return_counts=True)[1][1]}')
print(f'Passive days: {np.unique(labels(data), return_counts=True)[1][2]}')

print(f'The best day in terms of steps/calories: Day {best_steps_ratio(data)[2]}, '
      f'Ratio: {round(best_steps_ratio(data)[3], 2)}')

