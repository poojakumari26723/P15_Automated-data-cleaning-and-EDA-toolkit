from pathlib import Path
import pandas as pd

def load_dataset(file_path):
    """Load a CSV or Excel dataset after checking the file and extension."""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    suffix = path.suffix.lower()
    if suffix == ".csv":
        # Student performance datasets often use semicolons; infer delimiter.
        try:
            data = pd.read_csv(path, sep=None, engine="python")
            if data.shape[1] == 1:
                data = pd.read_csv(path, sep=";")
        except Exception:
            data = pd.read_csv(path)
    elif suffix in (".xlsx", ".xls"):
        data = pd.read_excel(path)
    else:
        raise ValueError("Please provide a CSV, XLSX, or XLS file.")
    if data.empty:
        raise ValueError("The dataset is empty.")
    return data
