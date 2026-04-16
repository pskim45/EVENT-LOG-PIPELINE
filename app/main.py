from generator import generate_events
from db import wait_for_db, insert_events
from analyze import (
    get_event_type_counts,
    get_user_event_counts,
    get_hourly_event_trend,
    get_error_ratio,
)
from visualize import ensure_output_dir, plot_event_type_counts, plot_hourly_event_trend

def main():
    print("[INFO] Pipeline started")

    wait_for_db() # MySQL이 준비될 때까지 대기

    events = generate_events(1000) # 1,000개의 이벤트를 무작위 생성
    print(f"[INFO] Generated {len(events)} events")

    insert_events(events)

    print("[INFO] Event type counts:", get_event_type_counts())
    print("[INFO] Top 5 user event counts:", get_user_event_counts()[:5])
    print("[INFO] Hourly event trend sample:", get_hourly_event_trend()[:5])
    print("[INFO] Error ratio:", get_error_ratio())

    ensure_output_dir()
    plot_event_type_counts()
    plot_hourly_event_trend()

    print("[INFO] Pipeline finished successfully")

if __name__ == "__main__":
    main()