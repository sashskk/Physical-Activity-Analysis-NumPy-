# Physical-Activity-Analysis-NumPy-
This project demonstrates a simple analysis of physical activity data (steps, calories burned, heart rate, and sleep duration) using Python and NumPy. It simulates one month's worth of daily activity data, performs basic statistical analysis, and categorizes days based on activity levels.
## Features
- Generates synthetic daily data for steps, calories, pulse, and sleep using NumPy.
- Calculates median steps, counts lazy days (steps < 5000), finds days with highest heart rate and longest sleep.
- Categorizes days into Active, Normal, or Passive based on step count, calorie burn, and sleep.
- Determines the day with the best steps-to-calories ratio.
- Outputs a concise monthly summary report.
## Project Structure
- generate_data.py — Generates synthetic activity data.
- analyze.py — Contains functions to analyze activity metrics.
- main.py — Runs the analysis and prints the summary report.
## Installation
This project requires Python 3.6+ and NumPy.
```bash
pip install numpy
```
## Usage
Run the main script to generate data and display the monthly activity summary:
## Author
Alexander
