from celery import Celery

celery_app = Celery(
    "distributed_task_system",
    broker = "amqp://guest:guest@rabbitmq:5672//",
    backend = "redis://redis:6379/0",
)

# Explicitly import tasks
import app.tasks.example_task

celery_app.conf.task_routes = {
    "app.tasks.*": {"queue": "default"},
}