## Exercise 2: Dockerized FastAPI CRUD APP
This is a simple **FastAPI-based CRUD (Create, Read, Update, Delete)** application built using **Python**
and a **virtual environment**. It allows you to manage a collection of student records via RESTful API endpoints.

## Features:
- ✅ Create a new student
- 🔍 Read student details by ID
- ♻️ Update existing student information
- 🗑️ Delete a student by ID
- ⚠️ Error handling using FastAPI's `HTTPException`
- 🌐 Interactive Swagger UI for testing the API

## 🧰 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- [Pydantic](https://docs.pydantic.dev/) (data validation)
- Docker (for containerization)

## 📁 Project Structure:

FastAPI_CRUD_APP/
 ├── __pycache__/           # Compiled Python files (auto-generated)
 ├── .dockerignore          # Specifies what to ignore during Docker build
 ├── Dockerfile             # Instructions to build the Docker image
 ├── main.py                # Main application file with FastAPI code
 ├── requirements.txt       # Python dependencies
├── README.md

## 🛠️ Setup Instructions(Without Docker):
1. **Clone the repository**  
   ```bash
   git clone https://github.com/saimanasreen001/FastAPI_CRUD_APP.git
   cd FastAPI_CRUD_APP
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   ```bash
   venv\Scripts\activate
   ```
4. **Install dependencies**
    ```bash
    pip install fastapi uvicorn pydantic
    pip install -r requirements.txt
    ```
5. **Add the dependencies to the requirements.txt file**
   ```bash
   pip freeze > requirements.txt
   ```

6. **Run the application**
    ```bash
    uvicorn main:app --reload
    ```
7. **Test the API**<br>
   Open http://127.0.0.1:8000/docs for the Swagger UI.
   
## Dockerized Deployment

1. **Docker Image**
   
   This app is already dockerized and available on Docker Hub:<br>
   https://hub.docker.com/r/saimanasreen/fastapi-crud-app
   

2. **Pull the Docker image**
   On any host machine with Docker installed:
   ```bash
   docker pull saimanasreen/fastapi-crud-app
   ```

3. **Run the Docker Container**
   ```bash
   docker run -d -p 8000:8000 saimanasreen/fastapi-crud-app
   ```
   The app will be accessible at http://localhost:8000/docs

   **Dockerfile Used**
   ```bash
   # Use an official Python base image
    FROM python:3.11-slim

   # Set the working directory
   WORKDIR /app

   # Copy requirements and install them
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy the rest of the app
   COPY main.py .
  
   # Command to run the app with uvicorn
   CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
  ```
   




