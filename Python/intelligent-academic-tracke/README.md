# Intelligent Academic Performance Tracker & Visualizer

A **Python** tool that loads student marks from CSV, cleans the data with **pandas**, computes GPA and identifies at-risk students, and displays a **Matplotlib** dashboard with:

- Histogram of GPA distribution
- Bar chart of department-wise average performance

## Features

- Import marks for 100+ students across 5 subjects from a CSV file
- Handle missing marks (mean, zero, or row-drop strategies)
- Compute total marks, percentage, and GPA (10-point scale)
- Flag "at-risk" students below a configurable pass threshold
- Visualize performance using an interactive Matplotlib dashboard

## Project Structure

```text
intelligent-academic-tracker/
│
├─ data/
│   └─ marks_sample.csv
│
├─ tracker/
│   ├─ __init__.py
│   ├─ config.py
│   ├─ data_loader.py
│   ├─ analytics.py
│   └─ visualization.py
│
├─ scripts/
│   └─ run_dashboard.py
│
├─ tests/
│   └─ test_analytics.py
│
├─ README.md
├─ requirements.txt
└─ .gitignore
