from pathlib import Path
import argparse
import sys

from eda_toolkit.loader import load_dataset
from eda_toolkit.cleaning import clean_dataset
from eda_toolkit.analysis import create_summary
from eda_toolkit.visualization import create_charts
from eda_toolkit.report import export_report

ROOT = Path(__file__).resolve().parent
DEFAULT_DATASET = ROOT / "datasets" / "student-mat.csv"
OUTPUT_DIR = ROOT / "output"

def main():
    parser = argparse.ArgumentParser(description="Automatically clean a dataset and create an EDA report.")
    parser.add_argument("dataset", nargs="?", default=str(DEFAULT_DATASET),
                        help="Path to a CSV or Excel file (default: datasets/student-mat.csv)")
    args = parser.parse_args()

    try:
        original = load_dataset(args.dataset)
        cleaned, cleaning_info = clean_dataset(original)
        numeric, categorical, missing = create_summary(cleaned)
        chart_names = create_charts(cleaned, OUTPUT_DIR)

        cleaned_path = OUTPUT_DIR / "cleaned_data.csv"
        cleaned.to_csv(cleaned_path, index=False)
        report_path = export_report(cleaned, numeric, categorical, missing, cleaning_info, chart_names, OUTPUT_DIR)

        print("\\n=== Automated Data Cleaning and EDA Toolkit ===")
        print(f"Input dataset: {args.dataset}")
        print(f"Original shape: {original.shape}")
        print(f"Cleaned shape: {cleaned.shape}")
        print(f"Missing values before cleaning: {cleaning_info['missing_values_before']}")
        print(f"Duplicate rows removed: {cleaning_info['duplicate_rows_removed']}")
        print("\\nNumeric summary:")
        print(numeric.to_string() if not numeric.empty else "No numeric columns found.")
        print(f"\\nCleaned data saved to: {cleaned_path}")
        print(f"EDA report saved to: {report_path}")
        print(f"Charts saved in: {OUTPUT_DIR}")
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
