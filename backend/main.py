from fastapi import FastAPI
from pydantic import BaseModel

class Job(BaseModel):
    name: str

app = FastAPI()

jobs = []
job_id = 0

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/jobs")
def get_jobs():
    return jobs

@app.post("/jobs")
def create_job(job: Job):
    global job_id

    new_job = {
        "id": job_id,
        "name": job.name
    }

    jobs.append(new_job)
    job_id += 1
    return new_job

# 
@app.put("/jobs/{job_id}")
def update_job(job_id: int, job: Job):
    for existing_jobs in jobs:
        if existing_jobs[job_id] == job_id:
            existing_jobs["name"].name == job.name
    return {"message" : "job not found"}
