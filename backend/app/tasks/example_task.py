from app.celery_app import celery_app
import time
import random

@celery_app.task(bind=True, max_retries=3)
def process_document_task(self, filename: str):
    """
    Simulates a heavy background task: extracting text, running OCR, 
    and generating embeddings for a document.
    """
    print(f"📄 [Worker] Starting processing for: {filename}")
    
    # Simulate a long-running task (e.g., PDF parsing or ML inference)
    for step in range(1, 4):
        time.sleep(2)  # 6 seconds total
        print(f"   [Worker] {filename}: Processing step {step}/3...")
        
    # Simulate a random failure (to show Celery retries in action)
    if random.random() < 0.2:  # 20% chance to fail on first try
        print(f"❌ [Worker] Failed to process {filename}. Retrying...")
        raise self.retry(exc=Exception("Simulated API timeout"), countdown=5)

    result = {
        "filename": filename,
        "status": "success",
        "pages_processed": random.randint(5, 50),
        "text_length": random.randint(1000, 5000)
    }
    
    print(f"✅ [Worker] Finished processing: {filename}")
    return result