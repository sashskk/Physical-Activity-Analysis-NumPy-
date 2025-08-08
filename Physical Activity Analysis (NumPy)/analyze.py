import numpy as np
from generate_data import activity_data

def average_steps(data):
    median_steps = np.median(data[:, 0])
    return median_steps

def lazy_days(data):
    lazy_steps_day = np.where(data[:, 0] < 5000)[0]
    return lazy_steps_day


def high_pulse_day(data):
    pulses = data[:, 2]
    max_pulse_index = np.argmax(pulses)
    max_pulse_day = pulses[max_pulse_index]
    return max_pulse_index + 1, max_pulse_day

def most_sleep_time(data):
    sleep = data[:, 3]
    max_sleep_index = np.argmax(sleep)
    max_sleep_time = sleep[max_sleep_index]
    return max_sleep_index + 1, max_sleep_time

def best_steps_ratio(data):
    steps = data[:, 0]
    calories = data[:, 1]
    ratio = steps / calories
    best_day_index = np.argmax(ratio)
    return steps,calories,best_day_index + 1,ratio[best_day_index]


def labels(data):
    conditions = np.empty(data.shape[0], dtype = object)
    active = (data[:, 0] > 10000) & (data[:, 1] > 2500)
    passive = (data[:, 0] < 5000) | (data[:, 3] < 5)
    conditions[:] = 'Normal'
    conditions[active] = 'Active'
    conditions[passive] = 'Passive'
    return conditions
