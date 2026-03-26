"""
Core analytics:
- GPA and percentage computation,
- at-risk student identification,
- department-level summaries.
"""

from __future__ import annotations

import pandas as pd


from .config import (
    SUBJECT_COLUMNS,
    MAX_MARKS_PER_SUBJECT,
    PASS_THRESHOLD,
    GPA_MAX,
)


def compute_gpa(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute total marks, percentage, and GPA for each student.

    Adds the following columns:
        - total_marks
        - percentage
        - gpa
    """
    df = df.copy()

    # Sum marks across all subject columns
    total_marks = df[SUBJECT_COLUMNS].sum(axis=1)

    max_total = MAX_MARKS_PER_SUBJECT * len(SUBJECT_COLUMNS)
    percentage = (total_marks / max_total) * 100.0

    # GPA scaled linearly from percentage, on a GPA_MAX scale.
    gpa = (percentage / 100.0) * GPA_MAX

    df["total_marks"] = total_marks
    df["percentage"] = percentage
    df["gpa"] = gpa

    return df


def mark_at_risk(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add an 'at_risk' boolean column based on PASS_THRESHOLD.

    A student is 'at_risk' if their percentage is below PASS_THRESHOLD.
    """
    df = df.copy()
    if "percentage" not in df.columns:
        raise ValueError("percentage column not found; run compute_gpa() first.")

    df["at_risk"] = df["percentage"] < PASS_THRESHOLD
    return df


def department_summary(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute department-wise average performance.

    Returns a new DataFrame with:
        - department
        - avg_percentage
        - avg_gpa
        - student_count
    """
    if "department" not in df.columns:
        raise ValueError("department column not found in DataFrame.")
    if "percentage" not in df.columns or "gpa" not in df.columns:
        raise ValueError("percentage/gpa columns not found; run compute_gpa() first.")

    grouped = (
        df.groupby("department")
        .agg(
            avg_percentage=("percentage", "mean"),
            avg_gpa=("gpa", "mean"),
            student_count=("student_id", "count"),
        )
        .reset_index()
    )

    return grouped
