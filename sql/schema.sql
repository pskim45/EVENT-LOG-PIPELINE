CREATE DATABASE IF NOT EXISTS event_pipeline;
USE event_pipeline;

CREATE TABLE IF NOT EXISTS events (
    event_id VARCHAR(36) PRIMARY KEY,
    event_type VARCHAR(50) NOT NULL,
    user_id VARCHAR(50) NOT NULL,
    event_time DATETIME NOT NULL
);

CREATE TABLE IF NOT EXISTS page_view_events (
    event_id VARCHAR(36) PRIMARY KEY,
    page_url VARCHAR(255) NOT NULL,
    CONSTRAINT fk_page_view_event
        FOREIGN KEY (event_id) REFERENCES events(event_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS purchase_events (
    event_id VARCHAR(36) PRIMARY KEY,
    product_id VARCHAR(50) NOT NULL,
    amount DECIMAL(10,2) NOT NULL,
    CONSTRAINT fk_purchase_event
        FOREIGN KEY (event_id) REFERENCES events(event_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS error_events (
    event_id VARCHAR(36) PRIMARY KEY,
    error_code VARCHAR(50) NOT NULL,
    error_message VARCHAR(255) NOT NULL,
    CONSTRAINT fk_error_event
        FOREIGN KEY (event_id) REFERENCES events(event_id)
        ON DELETE CASCADE
);

CREATE INDEX idx_events_type ON events(event_type);
CREATE INDEX idx_events_user ON events(user_id);
CREATE INDEX idx_events_time ON events(event_time);
