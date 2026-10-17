from fastapi import FastAPI
from celery.result import AsyncResult
from app.celery_app import celery_app
from app.routes.task_routes import router as task_router

app = FastAPI(
    title="Distributed Task System",
    description="Microservices architecture using FastAPI, Celery, RabbitMQ, and Redis",
    version="1.0.0"
)

app.include_router(task_router)

@app.get("/")
def health_check():
    return {"status": "healthy", "service": "api-gateway"}

@app.get("/tasks/status/{task_id}")
async def get_task_status(task_id: str):
    """Check the status and result of a specific background task"""
    task_result = AsyncResult(task_id, app=celery_app)
    
    response = {
        "task_id": task_id,
        "status": task_result.status,
    }
    
    if task_result.ready():
        response["result"] = task_result.result
    elif task_result.failed():
        response["error"] = str(task_result.result)
        
    return response