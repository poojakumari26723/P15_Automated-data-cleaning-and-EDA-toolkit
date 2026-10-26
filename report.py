from pathlib import Path
from datetime import datetime
import pandas as pd

def export_report(data, numeric_summary, categorical_summary, missing_summary, cleaning_info, chart_names, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    def table_html(frame):
        if frame is None or frame.empty:
            return "<p>No data available for this section.</p>"
        return frame.to_html(border=0, classes="data-table", na_rep="—")

    chart_html = "".join(
        f'<div class="chart"><h3>{name.replace("_", " ").replace(".png", "").title()}</h3>'
        f'<img src="{name}" alt="{name}"></div>'
        for name in chart_names
    ) or "<p>No numeric columns were available to create charts.</p>"

    outlier_rows = "".join(
        f"<li><b>{col}</b>: {count}</li>"
        for col, count in cleaning_info.get("outliers_by_column_iqr", {}).items()
    ) or "<li>No numeric columns available.</li>"

    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Automated Data Cleaning and EDA Report</title>
<style>
body{{font-family:Arial,sans-serif;max-width:1100px;margin:30px auto;padding:0 18px;color:#222;line-height:1.5}}
h1{{color:#163a5f}} h2{{border-bottom:2px solid #d9e2ec;padding-bottom:6px;margin-top:32px}}
.card{{background:#f3f6f9;padding:14px 18px;border-radius:8px;margin:12px 0}}
.data-table{{border-collapse:collapse;width:100%;font-size:13px;margin:12px 0;display:block;overflow-x:auto}}
.data-table th,.data-table td{{border:1px solid #ddd;padding:7px;text-align:left}}
.data-table th{{background:#e8eef5}} img{{max-width:100%;height:auto}} .chart{{margin:22px 0}}
</style></head><body>
<h1>Automated Data Cleaning and EDA Toolkit</h1>
<p>Generated on {datetime.now().strftime("%d %B %Y, %I:%M %p")}</p>
<h2>Dataset Overview</h2>
<div class="card"><p><b>Rows:</b> {len(data)} &nbsp; <b>Columns:</b> {len(data.columns)}</p>
<p><b>Missing values before cleaning:</b> {cleaning_info.get("missing_values_before", 0)}</p>
<p><b>Duplicate rows removed:</b> {cleaning_info.get("duplicate_rows_removed", 0)}</p>
<p><b>Rows after cleaning:</b> {cleaning_info.get("rows_after_cleaning", len(data))}</p></div>
<h2>Outlier Detection (IQR)</h2><ul>{outlier_rows}</ul>
<h2>Numeric Summary</h2>{table_html(numeric_summary)}
<h2>Categorical Summary</h2>{table_html(categorical_summary)}
<h2>Missing Values in Cleaned Data</h2>{table_html(missing_summary)}
<h2>Charts</h2>{chart_html}
</body></html>"""
    report_path = output_dir / "eda_report.html"
    report_path.write_text(html, encoding="utf-8")
    return report_path
