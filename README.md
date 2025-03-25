# Task Management API

![Python Version](https://img.shields.io/badge/python-3.11%2B-blue.svg)

## Table of Contents
- [Project Description](#project-description)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Project](#running-the-project)
    - [Locally](#running-locally)
    - [Using Docker](#running-using-docker)
- [API Endpoints](#api-endpoints)
- [Conclusion](#conclusion)

## Project Description

This is a Django-based Task Manager API that allows you to:
- Register users
- Assign tasks to users
- Fetch tasks for a specific user
- Return well-structured error and success responses
- Run with or without Docker

---

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.11 or higher
- pip
- Docker (If running using docker)
- SQLite

---

## Installation

### Clone the repository:

```bash
git clone https://github.com/sasha643/Joshtalks_backend_assessment.git
cd Joshtalks_backend_assessment
```

## Running the Project

### Running Locally

1. Create and activate virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

### Running using Docker

1. Build the Docker image:

```bash
docker build -t taskmanager-app .
```

2. Run the container:

```bash
docker run -p 8000:8000 taskmanager-app
```

**NOTE:** On container start, migrations will be applied automatically via entrypoint.sh and superuser will be created with credentials:  

username: admin  
email: admin@gmail.com  
password: admin123  


## API Endpoints

### 1. Register User

**POST** `http://127.0.0.1:8000/api/v1/users/register`

#### Request Body:

```bash
{
  "username": "saurabh1211",
  "email": "saurabh@example.com",
  "name": "saurabh",
  "mobile": "9876543210",
  "password": "testpass123"
}
```

#### Response Body:

```bash
{
  "reason": "Created",
  "message": "User registered successfully",
  "data": {
    "id": 1,
    "username": "saurabh1211",
    "name": "saurabh",
    "email": "saurabh@example.com",
    "mobile": "9876543210"
  }
}
```

### 2. Create Task

**POST** `http://127.0.0.1:8000/api/v1/tasks/create`

#### Request Body:

```bash
{
  "name": "Homepage UI Design",
  "description": "Design the initial wireframes and high-fidelity mockups for the homepage. Ensure responsiveness and alignment with the brand guidelines.",
  "task_type": "Design",
  "status": "Pending"
}
```

#### Response Body:

```bash
{
    "reason": "Created",
    "message": "Task created successfully"
}
```

### 3. Assign Task to a User

**POST** `http://127.0.0.1:8000/api/v1/tasks/assign`

#### Request Body:

```bash
{
  "task_id": 1,
  "user_ids": [1, 2, 3]
}
```

#### Response Body:

```bash
{
    "reason": "OK",
    "message": "Task assigned successfully"
}
```

### 4. Get Tasks for a Specific User

**GET** `http://127.0.0.1:8000/api/v1/tasks/users/<int:user_id>`

#### Response Body:

```bash
{
    "reason": "OK",
    "message": "Tasks fetched successfully",
    "data": [
        {
            "id": 2,
            "description": "Deploy the backend"
        },
        {
            "id": 1,
            "description": "Create the wireframe and UI for homepage"
        }
    ]
}
```

**NOTE**:
If you're running the application using Docker, replace 127.0.0.1 with localhost in the API URLs.
Example:
```http://127.0.0.1:8000 ``` → ```http://localhost:8000 ```


## Conclusion

The APIs in this project are properly versioned under ```/api/v1/```, ensuring future scalability and backward compatibility.

For further optimization and enhancement, consider the following:

- Implementing **pagination** for endpoints like Get Tasks, especially when the task list grows large.
- Adding **token-based authentication** (e.g., JWT or session-based auth) to secure API access and associate data with authenticated users.

These improvements will make the API more robust, secure, and production-ready.
