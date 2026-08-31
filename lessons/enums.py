from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class TaskStatus(str, Enum):
    todo = "todo"
    in_progress = "in_progress"
    review = "review"
    completed = "completed"
    cancelled = "cancelled"

class Priority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"

@app.get("/tasks/{status}")
def get_status(status: TaskStatus):
    if status is TaskStatus.todo:
        return {
            "status": status,
            "message": "Task hasn't started yet."
        }
    if status is TaskStatus.in_progress:
        return {
            "status": status,
            "message": "Task is currently being worked on."
        }
    if status is TaskStatus.review:
        return {
            "status": status,
            "message": "Task is waiting for review."
        }
    if status is TaskStatus.completed:
        return {
            "status": status,
            "message": "Task has been completed."
        }
    if status is TaskStatus.cancelled:
        return {
            "status": status,
            "message": "Task has been cancelled."
        }
    return None

@app.get("/tasks/priority/{priority}")
def get_priority(priority: Priority):
    if priority is Priority.low:
        return {
            "priority": priority,
            "message": "Priority is too low for this task."
        }
    if priority is Priority.medium:
        return {
            "priority": priority,
            "message": "Priority is perfect for the task."
        }
    if priority is Priority.high:
        return {
            "priority": priority,
            "message": "Priority is high for this task."
        }
    if priority is Priority.urgent:
        return {
            "priority": priority,
            "message": "Priority in urgency not allowed."
        }
    return None

@app.get("/tasks/{status}/{priority}")
def get_both(status: TaskStatus, priority: Priority):
    if status is TaskStatus.completed:
        return {
            "status": status,
            "message": "Task has been finished."
        }
    if status is TaskStatus.cancelled:
        return {
            "status": status,
            "message": "Task has been cancelled."
        }
    if status is TaskStatus.todo and priority is Priority.urgent:
        return {
            "status": status,
            "priority": priority,
            "message": "It's an urgent task that hasn't started."
        }
    if status is TaskStatus.in_progress and priority is Priority.urgent:
        return {
            "status": status,
            "priority": priority,
            "message": "It's an urgent task currently being worked on."
        }
    if status is TaskStatus.review and priority is Priority.high:
        return {
            "status": status,
            "priority": priority,
            "message": "It's a high priority task waiting for review."
        }
    return {
        "status": status,
        "priority": priority,
        "message": "No special conditions for this task."
    }