from db import get_connection

def get_event_type_counts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT event_type, COUNT(*) AS count
        FROM events
        GROUP BY event_type
        ORDER BY count DESC
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_user_event_counts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_id, COUNT(*) AS total_events
        FROM events
        GROUP BY user_id
        ORDER BY total_events DESC
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_hourly_event_trend():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DATE_FORMAT(event_time, '%Y-%m-%d %H:00:00') AS event_hour, COUNT(*) AS count
        FROM events
        GROUP BY event_hour
        ORDER BY event_hour
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_error_ratio():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT ROUND(
            100.0 * SUM(CASE WHEN event_type = 'error' THEN 1 ELSE 0 END) / COUNT(*),
            2
        ) AS error_ratio_percent
        FROM events
    """)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row[0]