# P-15: Automated Data Cleaning and EDA Toolkit

This beginner-friendly Python project uses the supplied `student-mat.csv` dataset by default.

## Features
- Loads CSV and Excel files with basic validation.
- Fills missing numeric values with the median and text values with the most common value.
- Removes duplicate rows.
- Detects outliers using the IQR rule and reports the count per numeric column.
- Creates numeric and categorical summary statistics.
- Generates histograms, box plots, and a correlation heatmap.
- Exports the cleaned CSV and an HTML EDA report.

## Folder structure
```text
P15_Automated_Data_Cleaning_EDA_Toolkit/
├── datasets/
│   └── student-mat.csv
├── eda_toolkit/
│   ├── __init__.py
│   ├── loader.py
│   ├── cleaning.py
│   ├── analysis.py
│   ├── visualization.py
│   └── report.py
├── output/
├── main.py
├── requirements.txt
└── README.md
```

## Run in VS Code (Windows)
1. Extract the ZIP file.
2. Open the `P15_Automated_Data_Cleaning_EDA_Toolkit` folder in VS Code.
3. Open Terminal → New Terminal.
4. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
5. Run the project:
   ```bash
   python main.py
   ```
6. Open the `output` folder. It will contain `cleaned_data.csv`, `eda_report.html`, and chart images.

## Use another dataset
```bash
python main.py "datasets/another_dataset.csv"
```
Excel files are also supported:
```bash
python main.py "datasets/another_dataset.xlsx"
```

## Notes
- This is an educational project; review the cleaning choices before using the output for important decisions.
- The IQR outlier counts are reported, not automatically deleted, to avoid losing potentially useful data.
