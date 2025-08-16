import os
from faker import Faker
import datetime
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Initialize Faker for synthetic data
fake = Faker()

def generate_synthetic_smartsheet_data(num_rows=10):
    """Generate fake Smartsheet data for demo mode."""
    today = datetime.date.today()
    data = []
    for _ in range(num_rows):
        due_date = today + datetime.timedelta(days=fake.random_int(min=1, max=7))
        task_name = fake.sentence(nb_words=3)
        assignee = fake.email()
        data.append({
            "id": fake.uuid4(),
            "due_date": due_date.strftime('%Y-%m-%d'),
            "task_name": task_name,
            "assignee": assignee,
            "status": "Pending"
        })
    return data

def simulate_gmail_draft(task):
    """Simulate creating a Gmail draft and log the result."""
    subject = f"Task Reminder: {task['task_name']}"
    body = f"Hi {task['assignee'].split('@')[0]},\n\nTask '{task['task_name']}' is due on {task['due_date']}. Please complete it soon.\n\nBest,\nYour Automation Team"
    logger.info(f"Simulated Gmail Draft Created - Subject: {subject}\nBody: {body}")
    return {"draft_id": fake.uuid4()}  # Fake draft ID

def update_synthetic_status(tasks, task_id, new_status):
    """Update the status of a synthetic task."""
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            logger.info(f"Updated task {task_id} status to {new_status}")
            break

def main():
    """Main function to run the demo automation."""
    # Check demo mode from environment
    demo_mode = os.getenv("DEMO_MODE", "false").lower() == "true"
    if not demo_mode:
        logger.warning("Demo mode is disabled. This script is designed for demo use only.")
        return

    logger.info("Starting Smartsheet + Gmail Automation in Demo Mode")

    # Generate synthetic data
    tasks = generate_synthetic_smartsheet_data()
    logger.info(f"Generated {len(tasks)} synthetic tasks")

    # Process each task
    for task in tasks:
        if task["status"] == "Pending":
            draft = simulate_gmail_draft(task)
            update_synthetic_status(tasks, task["id"], "Notification Sent")
            logger.info(f"Processed task {task['id']} with draft {draft['draft_id']}")

    logger.info("Automation completed. Check logs for simulated drafts.")

if __name__ == "__main__":
    main()