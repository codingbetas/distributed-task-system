from fastapi import APIRouter
from pydantic import BaseModel
from app.tasks.example_task import process_document_task

router = APIRouter()

class TaskRequest(BaseModel):
    filename: str

@router.post("/tasks/submit")
def submit_task(request: TaskRequest):
    # Send the task to RabbitMQ
    task = process_document_task.delay(request.filename)
    return {
        "message": "Task submitted successfully",
        "task_id": task.id
    }