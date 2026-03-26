"""
Data loading and cleaning utilities using pandas.
"""

from __future__ import annotations

from typing import Literal

import pandas as pd

from .config import SUBJECT_COLUMNS


def load_marks_csv(path: str) -> pd.DataFrame:
    """
    Load the marks CSV into a pandas DataFrame.

    Expected columns:
        - student_id
        - student_name
        - department
        - subject1 ... subject5 (or as defined in SUBJECT_COLUMNS)
    """
    df = pd.read_csv(path)
    return df


def clean_marks(
    df: pd.DataFrame,
    strategy: Literal["mean", "zero", "drop"] = "mean",
) -> pd.DataFrame:
    """
    Handle missing marks in the subject columns.

    Parameters
    ----------
    df : DataFrame
        Raw marks DataFrame.
    strategy : {"mean", "zero", "drop"}
        - "mean": fill NaN in each subject with that subject's column mean.
        - "zero": fill NaN with 0.
        - "drop": drop rows that have any NaN in subject columns.

    Returns
    -------
    DataFrame
        Cleaned DataFrame.
    """
    df = df.copy()

    if strategy == "zero":
        df[SUBJECT_COLUMNS] = df[SUBJECT_COLUMNS].fillna(0)
    elif strategy == "mean":
        # Fill NaN in each subject column with column-wise mean.[web:17][web:19][web:26]
        for col in SUBJECT_COLUMNS:
            if col in df.columns:
                col_mean = df[col].mean()
                df[col] = df[col].fillna(col_mean)
    elif strategy == "drop":
        df = df.dropna(subset=SUBJECT_COLUMNS)
    else:
        raise ValueError(f"Unknown strategy: {strategy}")

    return df
