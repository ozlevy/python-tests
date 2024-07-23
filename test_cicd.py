import requests

BASE_URL = "http://localhost:8080"

def test_get_all_jobs():
    response = requests.get(f"{BASE_URL}/jobs")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_job():
    new_job = {
        "jobName": "New Job",
        "status": "Pending",
        "jobType": "Build"
    }
    response = requests.post(f"{BASE_URL}/jobs", json=new_job)
    assert response.status_code == 201
    job = response.json()
    assert job["jobName"] == new_job["jobName"]
    assert job["status"] == new_job["status"]
    assert job["jobType"] == new_job["jobType"]

def test_get_job_by_id():
    # Create a new job
    new_job = {
        "jobName": "New Job",
        "status": "Pending",
        "jobType": "Build"
    }
    response = requests.post(f"{BASE_URL}/jobs", json=new_job)
    assert response.status_code == 201
    job = response.json()
    job_id = job["id"]

    # Retrieve the job by ID
    response = requests.get(f"{BASE_URL}/jobs/{job_id}")
    assert response.status_code == 200
    job = response.json()
    assert job["id"] == job_id

def test_update_job_status():
    # Create a new job
    new_job = {
        "jobName": "New Job",
        "status": "Pending",
        "jobType": "Build"
    }
    response = requests.post(f"{BASE_URL}/jobs", json=new_job)
    assert response.status_code == 201
    job = response.json()
    job_id = job["id"]

    # Update the job status
    updated_status = {"status": "In Progress"}
    response = requests.put(f"{BASE_URL}/jobs/{job_id}", json=updated_status)
    assert response.status_code == 200
    job = response.json()
    assert job["status"] == updated_status["status"]

def test_delete_job():
    # Create a new job
    new_job = {
        "jobName": "New Job",
        "status": "Pending",
        "jobType": "Build"
    }
    response = requests.post(f"{BASE_URL}/jobs", json=new_job)
    assert response.status_code == 201
    job = response.json()
    job_id = job["id"]

    # Delete the job
    response = requests.delete(f"{BASE_URL}/jobs/{job_id}")
    assert response.status_code == 204
