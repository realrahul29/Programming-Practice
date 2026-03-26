"""
Intelligent Academic Performance Tracker & Visualizer.

This package provides tools to:
- load and clean marks data from CSV,
- compute GPA and identify at-risk students,
- generate visual dashboards using Matplotlib.
"""

from .config import PASS_THRESHOLD, MAX_MARKS_PER_SUBJECT, SUBJECT_COLUMNS
from .data_loader import load_marks_csv, clean_marks
from .analytics import compute_gpa, mark_at_risk, department_summary
from .visualization import plot_dashboard

__all__ = [
    "PASS_THRESHOLD",
    "MAX_MARKS_PER_SUBJECT",
    "SUBJECT_COLUMNS",
    "load_marks_csv",
    "clean_marks",
    "compute_gpa",
    "mark_at_risk",
    "department_summary",
    "plot_dashboard",
]
