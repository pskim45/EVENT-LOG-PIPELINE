import os
import matplotlib.pyplot as plt
from analyze import get_event_type_counts, get_hourly_event_trend

OUTPUT_DIR = "/app/output"

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def plot_event_type_counts():
    rows = get_event_type_counts()
    labels = [row[0] for row in rows]
    values = [row[1] for row in rows]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.title("Event Type Counts")
    plt.xlabel("Event Type")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/event_type_counts.png")
    plt.close()

def plot_hourly_event_trend():
    rows = get_hourly_event_trend()
    labels = [row[0] for row in rows]
    values = [row[1] for row in rows]

    plt.figure(figsize=(12, 5))
    plt.plot(labels, values, marker="o")
    plt.title("Hourly Event Trend")
    plt.xlabel("Hour")
    plt.ylabel("Count")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_DIR}/hourly_event_trend.png")
    plt.close()