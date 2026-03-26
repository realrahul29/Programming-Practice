#!/usr/bin/env python3
"""
CLI entry point for the Intelligent Academic Performance Tracker.

Usage:
    python scripts/run_dashboard.py
    python scripts/run_dashboard.py --csv path/to/your_file.csv
"""

import argparse
import os
import sys

# Allow importing the 'tracker' package when running from project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from tracker.data_loader import load_marks_csv, clean_marks
from tracker.analytics import compute_gpa, mark_at_risk
from tracker.visualization import plot_dashboard


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Academic Performance Dashboard."
    )
    parser.add_argument(
        "--csv",
        type=str,
        default=os.path.join(PROJECT_ROOT, "data", "marks_sample.csv"),
        help="Path to marks CSV file (default: data/marks_sample.csv)",
    )
    parser.add_argument(
        "--clean-strategy",
        type=str,
        choices=["mean", "zero", "drop"],
        default="mean",
        help="Strategy to handle missing marks (default: mean).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    print(f"Loading data from: {args.csv}")
    df = load_marks_csv(args.csv)
    df = clean_marks(df, strategy=args.clean_strategy)
    df = compute_gpa(df)
    df = mark_at_risk(df)

    print(df.head())
    print(f"Total students: {len(df)}")
    print(f"At-risk students (< 40%): {df['at_risk'].sum()}")

    plot_dashboard(df)


if __name__ == "__main__":
    main()
