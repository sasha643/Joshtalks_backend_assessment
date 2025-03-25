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
- [API Example](#api-example)
- [Swagger UI](#swagger-ui)

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
- Docker
- SQLite

---

## Installation

### Clone the repository:

```bash
git clone https://github.com/sasha643/Joshtalks_backend_assessment.git
cd Joshtalks_backend_assessment

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
