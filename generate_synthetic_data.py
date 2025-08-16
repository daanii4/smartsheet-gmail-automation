import csv
from faker import Faker
import random
from datetime import datetime

# Initialize Faker
fake = Faker()

# Generate 10 fake rows for Smartsheet (tasks with details)
rows = []
for _ in range(10):
    task_name = fake.sentence(nb_words=6).rstrip('.')  # Fake task name, remove trailing period
    assignee = fake.name()  # Fake assignee name (user)
    due_date = fake.date_between(start_date='today', end_date='+60d').strftime('%Y-%m-%d')  # Due date in next 60 days, formatted as string
    paid_status = random.choice(['Yes', 'No'])  # Random payment status
    additional_details = fake.paragraph(nb_sentences=2)  # Add some detailed description for the task
    
    rows.append({
        'Task Name': task_name,
        'Assignee': assignee,
        'Due Date': due_date,
        'Paid': paid_status,
        'Details': additional_details
    })

# Save to CSV file (can be imported into Smartsheet)
csv_filename = 'synthetic_data.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    fieldnames = ['Task Name', 'Assignee', 'Due Date', 'Paid', 'Details']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"Generated 10 fake Smartsheet rows and saved to {csv_filename}")