from backend.app.celery_app import celery_app
celery_app.autodiscover_tasks(['backend.app.tasks'])
# Start Celery worker from project root:
# celery -A celery_worker.worker.celery_app worker --loglevel=info