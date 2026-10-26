import pandas as pd

def clean_dataset(data):
    """Fill missing values, remove duplicate rows, and flag IQR outliers."""
    cleaned = data.copy()
    missing_before = int(cleaned.isna().sum().sum())
    duplicates_before = int(cleaned.duplicated().sum())

    for col in cleaned.columns:
        if cleaned[col].isna().any():
            if pd.api.types.is_numeric_dtype(cleaned[col]):
                median = cleaned[col].median()
                cleaned[col] = cleaned[col].fillna(median)
            else:
                mode = cleaned[col].mode(dropna=True)
                replacement = mode.iloc[0] if not mode.empty else "Unknown"
                cleaned[col] = cleaned[col].fillna(replacement)

    cleaned = cleaned.drop_duplicates().reset_index(drop=True)

    outlier_counts = {}
    numeric_cols = cleaned.select_dtypes(include="number").columns
    for col in numeric_cols:
        series = cleaned[col].dropna()
        if len(series) < 4:
            continue
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        if iqr == 0:
            outlier_counts[col] = 0
        else:
            low, high = q1 - 1.5 * iqr, q3 + 1.5 * iqr
            outlier_counts[col] = int(((series < low) | (series > high)).sum())

    info = {
        "missing_values_before": missing_before,
        "duplicate_rows_removed": duplicates_before,
        "rows_after_cleaning": len(cleaned),
        "outliers_by_column_iqr": outlier_counts,
    }
    return cleaned, info
