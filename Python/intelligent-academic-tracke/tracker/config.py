"""
Configuration constants for the Intelligent Academic Performance Tracker.
"""

# Minimum passing percentage, used to flag at-risk students
PASS_THRESHOLD: float = 40.0

# Maximum marks per subject (assumed same for all subjects)
MAX_MARKS_PER_SUBJECT: float = 100.0

# Columns in the CSV that correspond to subjects
SUBJECT_COLUMNS = ["subject1", "subject2", "subject3", "subject4", "subject5"]

# GPA scale (e.g., 10-point scale)
GPA_MAX: float = 10.0
