"""
Visualization module using Matplotlib.

Provides:
- Histogram of GPA distribution.
- Bar chart of department-wise average performance.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import pandas as pd

from .analytics import department_summary


def plot_dashboard(df: pd.DataFrame) -> None:
    """
    Create a simple dashboard with:
        - Histogram of GPA distribution.
        - Bar chart of department-wise average percentage.

    This function displays the plots using plt.show().
    """
    if "gpa" not in df.columns or "percentage" not in df.columns:
        raise ValueError("DataFrame must have 'gpa' and 'percentage' columns.")

    # Prepare figure with two subplots: histogram and bar chart.[web:9][web:12][web:27]
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    # 1) Histogram of GPA distribution
    axes[0].hist(df["gpa"], bins=10, color="skyblue", edgecolor="black")
    axes[0].set_title("GPA Distribution")
    axes[0].set_xlabel("GPA")
    axes[0].set_ylabel("Number of Students")

    # 2) Bar chart of department-wise average percentage
    dept_stats = department_summary(df)

    axes[1].bar(
        dept_stats["department"],
        dept_stats["avg_percentage"],
        color="orange",
        edgecolor="black",
    )
    axes[1].set_title("Department-wise Average Percentage")
    axes[1].set_xlabel("Department")
    axes[1].set_ylabel("Average Percentage")
    axes[1].tick_params(axis="x", rotation=45)

    plt.tight_layout()
    plt.show()
