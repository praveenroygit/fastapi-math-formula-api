# FastAPI Math Formula API

A beginner-friendly FastAPI project that demonstrates API creation, request validation, Swagger testing, and MySQL CRUD integration.

## Features

- FastAPI backend
- Swagger UI documentation
- Pydantic request validation
- MySQL database connection
- Create, Read, Update, Delete calculations
- Clean separation using `main.py`, `crud.py`, and `database.py`

## Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn
- MySQL
- MySQL Connector Python

## Run Locally

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload



## Database Configuration

Update the database credentials in `database.py` before running the project.pwd