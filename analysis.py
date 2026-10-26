import pandas as pd

def create_summary(data):
    """Return descriptive statistics for numeric and categorical columns."""
    numeric = data.describe(include="number").transpose()
    categorical = data.describe(include=["object", "category", "bool"]).transpose()
    missing = data.isna().sum().rename("missing_values").to_frame()
    return numeric, categorical, missing

def correlation_matrix(data):
    numeric = data.select_dtypes(include="number")
    if numeric.shape[1] < 2:
        return None
    return numeric.corr()
