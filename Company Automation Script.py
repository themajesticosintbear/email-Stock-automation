#!/usr/bin/env python3

import datetime
import smtplib
from email.mime.text import MIMEText

# --- DeliBear Company Automation Script ---

COMPANY_NAME = "DeliBear Company"
CONTACT_EMAIL = "contact@delibearcompany.eu"
Company_site = "https://delibearcompany.wordpress.com/"

def log_activity(message):
    """Logs an activity with a timestamp."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")

def check_stock_levels(items):
    """Checks the stock levels of provided items and alerts if low."""
    log_activity("Checking stock levels...")
    low_stock_items = {}
    # In a real scenario, this would connect to a database or inventory system
    inventory = {
        "Sliced Ham": 50,
        "Swiss Cheese": 30,
        "Baguettes": 100,
        "Tomatoes": 25,
        "Lettuce Heads": 15,
        "Mustard Jars": 10,
    }

    LOW_STOCK_THRESHOLD = 20

    for item in items:
        if item in inventory:
            if inventory[item] < LOW_STOCK_THRESHOLD:
                low_stock_items[item] = inventory[item]
                log_activity(f"WARNING: Low stock for {item} ({inventory[item]} remaining)")
        else:
            log_activity(f"ERROR: Item '{item}' not found in inventory.")
    return low_stock_items

def generate_low_stock_report(low_stock_items):
    """Generates a report of items with low stock."""
    if not low_stock_items:
        return "All items are currently above the low stock threshold."

    report = "--- Low Stock Report ---\n"
    for item, quantity in low_stock_items.items():
        report += f"- {item}: {quantity} remaining\n"
    report += f"\nPlease consider restocking these items soon.\n\nSincerely,\nThe DeliBear Automation System"
    return report

def send_email_alert(subject, body, recipient_email=CONTACT_EMAIL):
    """Sends an email with the given subject and body."""
    log_activity(f"Sending email alert to {recipient_email}...")
    sender_email = "automation@delibearcompany.eu"  # Replace with a valid sender email
    sender_password = "your_password"  # Replace with the actual password

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = recipient_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
        log_activity("Email sent successfully!")
    except Exception as e:
        log_activity(f"ERROR: Could not send email. {e}")

def process_daily_orders():
    """Simulates processing daily orders."""
    log_activity("Processing daily orders...")
    # In a real scenario, this would involve reading order data,
    # updating inventory, and potentially generating packing slips.
    orders = [
        {"item": "Sliced Ham Sandwich", "quantity": 10},
        {"item": "Swiss Cheese and Tomato Baguette", "quantity": 5},
        {"item": "Mustard", "quantity": 2},
    ]
    log_activity(f"Simulated processing of {len(orders)} orders.")
    # Further logic to update inventory based on orders would go here

def schedule_tasks():
    """Simulates scheduled daily tasks."""
    log_activity("Running scheduled daily tasks...")
    items_to_check = ["Sliced Ham", "Swiss Cheese", "Baguettes", "Tomatoes", "Lettuce Heads", "Mustard Jars"]
    low_stock = check_stock_levels(items_to_check)

    if low_stock:
        report = generate_low_stock_report(low_stock)
        send_email_alert("Low Stock Alert", report)
    else:
        log_activity("Stock levels are healthy.")

    process_daily_orders()
    log_activity("Daily tasks completed.")

if __name__ == "__main__":
    log_activity(f"Starting automation script for {COMPANY_NAME}...")
    schedule_tasks()
    log_activity("Automation script finished.")
