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
- Docker & Docker Compose (optional for Dockerized setup)
- PostgreSQL (or SQLite for local testing)

---

## Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/taskmanager.git
cd taskmanager
