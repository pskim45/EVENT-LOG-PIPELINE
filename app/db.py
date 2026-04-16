import time
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="db",
        port=3306,
        user="root",
        password="root",
        database="event_pipeline"
    )

def wait_for_db(max_retries=20, delay=3):
    for attempt in range(1, max_retries + 1):
        try:
            conn = get_connection()
            conn.close()
            print("[INFO] MySQL connection successful")
            return
        except Exception as e:
            print(f"[INFO] Waiting for MySQL... ({attempt}/{max_retries}) - {e}")
            time.sleep(delay)
    raise Exception("MySQL connection failed after retries")

def insert_event(cursor, event):
    cursor.execute(
        """
        INSERT INTO events (event_id, event_type, user_id, event_time)
        VALUES (%s, %s, %s, %s)
        """,
        (
            event["event_id"],
            event["event_type"],
            event["user_id"],
            event["event_time"].strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    if event["event_type"] == "page_view":
        cursor.execute(
            """
            INSERT INTO page_view_events (event_id, page_url)
            VALUES (%s, %s)
            """,
            (event["event_id"], event["page_url"])
        )

    elif event["event_type"] == "purchase":
        cursor.execute(
            """
            INSERT INTO purchase_events (event_id, product_id, amount)
            VALUES (%s, %s, %s)
            """,
            (event["event_id"], event["product_id"], event["amount"])
        )

    elif event["event_type"] == "error":
        cursor.execute(
            """
            INSERT INTO error_events (event_id, error_code, error_message)
            VALUES (%s, %s, %s)
            """,
            (event["event_id"], event["error_code"], event["error_message"])
        )

def insert_events(events):
    conn = get_connection()
    cursor = conn.cursor()

    for event in events:
        insert_event(cursor, event)

    conn.commit()
    print(f"[INFO] Inserted {len(events)} events into MySQL")

    cursor.close()
    conn.close()