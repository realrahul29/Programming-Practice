"""
Basic unit tests for analytics functions.
Run with:  pytest
"""

import pandas as pd

from tracker.analytics import compute_gpa, mark_at_risk, department_summary
from tracker.config import SUBJECT_COLUMNS, PASS_THRESHOLD, MAX_MARKS_PER_SUBJECT, GPA_MAX


def _sample_df():
    # minimal sample dataset with two departments
    data = {
        "student_id": [1, 2, 3],
        "student_name": ["A", "B", "C"],
        "department": ["CS", "CS", "IT"],
        SUBJECT_COLUMNS[0]: [80, 30, 50],
        SUBJECT_COLUMNS[1]: [70, 20, 60],
        SUBJECT_COLUMNS[2]: [90, 25, 70],
        SUBJECT_COLUMNS[3]: [85, 35, 65],
        SUBJECT_COLUMNS[4]: [75, 40, 55],
    }
    return pd.DataFrame(data)


def test_compute_gpa():
    df = _sample_df()
    result = compute_gpa(df)

    assert "total_marks" in result.columns
    assert "percentage" in result.columns
    assert "gpa" in result.columns

    max_total = MAX_MARKS_PER_SUBJECT * len(SUBJECT_COLUMNS)
    expected_percentage = (result.loc[0, "total_marks"] / max_total) * 100.0
    expected_gpa = (expected_percentage / 100.0) * GPA_MAX

    assert result.loc[0, "percentage"] == expected_percentage
    assert result.loc[0, "gpa"] == expected_gpa


def test_mark_at_risk():
    df = _sample_df()
    df = compute_gpa(df)
    result = mark_at_risk(df)

    assert "at_risk" in result.columns
    # At least one student should be at risk based on the sample data.
    assert result["at_risk"].dtype == bool
    assert (result["percentage"] < PASS_THRESHOLD).equals(result["at_risk"])


def test_department_summary():
    df = _sample_df()
    df = compute_gpa(df)
    summary = department_summary(df)

    # Should have two departments: CS and IT
    assert set(summary["department"]) == {"CS", "IT"}
    assert "avg_percentage" in summary.columns
    assert "avg_gpa" in summary.columns
    assert "student_count" in summary.columns

    # student_count should add up
    assert summary["student_count"].sum() == len(df)
