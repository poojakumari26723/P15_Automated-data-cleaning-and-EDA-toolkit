from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import seaborn as sns

def create_charts(data, output_dir):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    numeric_cols = list(data.select_dtypes(include="number").columns)
    paths = []

    if numeric_cols:
        # Histograms
        data[numeric_cols].hist(figsize=(12, 8), bins=15, edgecolor="black")
        plt.suptitle("Histograms of Numeric Columns")
        plt.tight_layout()
        p = output_dir / "histograms.png"
        plt.savefig(p, dpi=150)
        plt.close("all")
        paths.append(p.name)

        # Box plots
        count = min(len(numeric_cols), 8)
        plt.figure(figsize=(max(8, count * 1.4), 5))
        sns.boxplot(data=data[numeric_cols[:count]], orient="h")
        plt.title("Box Plots of Numeric Columns")
        plt.tight_layout()
        p = output_dir / "boxplots.png"
        plt.savefig(p, dpi=150)
        plt.close()
        paths.append(p.name)

    if len(numeric_cols) >= 2:
        plt.figure(figsize=(10, 8))
        sns.heatmap(data[numeric_cols].corr(), cmap="coolwarm", center=0, annot=False)
        plt.title("Correlation Heatmap")
        plt.tight_layout()
        p = output_dir / "correlation_heatmap.png"
        plt.savefig(p, dpi=150)
        plt.close()
        paths.append(p.name)

    return paths
