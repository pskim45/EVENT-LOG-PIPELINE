import random
import uuid
from datetime import datetime, timedelta

EVENT_TYPES = ["page_view", "purchase", "error"]
PAGES = ["/", "/login", "/products", "/cart", "/checkout", "/mypage"]
PRODUCTS = ["P100", "P200", "P300", "P400"]
ERROR_CODES = ["500", "404", "403", "TIMEOUT"]

def random_event():
    event_type = random.choice(EVENT_TYPES)

    event = {
        "event_id": str(uuid.uuid4()),
        "event_type": event_type,
        "user_id": f"user_{random.randint(1, 20)}",
        "event_time": datetime.now() - timedelta(minutes=random.randint(0, 1440))
    }

    if event_type == "page_view":
        event["page_url"] = random.choice(PAGES)

    elif event_type == "purchase":
        event["product_id"] = random.choice(PRODUCTS)
        event["amount"] = round(random.uniform(10, 500), 2)

    elif event_type == "error":
        event["error_code"] = random.choice(ERROR_CODES)
        event["error_message"] = "sample error occurred"

    return event

def generate_events(count=1000):
    return [random_event() for _ in range(count)]
