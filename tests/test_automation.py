import datetime
import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from automation import generate_synthetic_smartsheet_data, simulate_gmail_draft, update_synthetic_status

def test_generate_synthetic_data():
    tasks = generate_synthetic_smartsheet_data()
    assert len(tasks) == 10  # Default value when NUM_TASKS is not set
    assert all("due_date" in task for task in tasks)
    assert all(datetime.datetime.strptime(task["due_date"], '%Y-%m-%d').date() >= datetime.date.today() for task in tasks)

def test_simulate_gmail_draft():
    task = {"task_name": "Test Task", "assignee": "test@example.com", "due_date": "2025-08-17"}
    draft = simulate_gmail_draft(task)
    assert "draft_id" in draft
    assert isinstance(draft["draft_id"], str)

def test_update_synthetic_status():
    # Set NUM_TASKS to 1 for this test
    import os
    original_num_tasks = os.environ.get("NUM_TASKS")
    os.environ["NUM_TASKS"] = "1"
    
    tasks = generate_synthetic_smartsheet_data()
    task_id = tasks[0]["id"]
    update_synthetic_status(tasks, task_id, "Done")
    assert tasks[0]["status"] == "Done"
    
    # Restore original environment
    if original_num_tasks:
        os.environ["NUM_TASKS"] = original_num_tasks
    else:
        del os.environ["NUM_TASKS"]

def test_num_tasks_env():
    import os
    os.environ["NUM_TASKS"] = "3"
    tasks = generate_synthetic_smartsheet_data()
    assert len(tasks) == 3
    del os.environ["NUM_TASKS"]