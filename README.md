## Exercise 2: FastAPI CRUD APP with JWT Authentication
This is a simple **FastAPI-based CRUD (Create, Read, Update, Delete)** application built using **Python** and a **virtual environment**. It allows you to manage a collection of student records via RESTful API endpoints.

Now with **JWT Authentication**: All student endpoints are protected and require a valid JSON Web Token (JWT) for access.

## Features:
- ✅ Create a new student
- 🔍 Read student details by ID
- ♻️ Update existing student information
- 🗑️ Delete a student by ID
- 🔒 JWT Authentication for all endpoints
- ⚠️ Error handling using FastAPI's `HTTPException`
- 🌐 Interactive Swagger UI for testing the API

## 🧰 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI server)
- [Pydantic](https://docs.pydantic.dev/) (data validation)
- [python-jose](https://python-jose.readthedocs.io/en/latest/) (JWT)
- [passlib](https://passlib.readthedocs.io/en/stable/) (password hashing)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (env vars)
- Docker (for containerization)

## 📁 Project Structure:

FastAPI_CRUD_APP/<br>
 ├── __pycache__/          <br>
 ├── .env                  <br>
 ├── Dockerfile            <br>
 ├── main.py               <br>
 ├── auth.py               <br>
 ├── requirements.txt      <br>
 ├── README.md

## 🛠️ Setup Instructions (Without Docker):
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
   .\venv\Scripts\activate
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
    uvicorn FastAPI_CRUD_APP.main:app --reload
    ```

7. **Test the API with JWT Authentication**
   - Open http://127.0.0.1:8000/docs for the Swagger UI.
   - **Get a JWT Token:**
     1. Find the `/token` endpoint (POST) in Swagger UI.
     2. Click "Try it out".
     3. Enter:
        - username: `admin`
        - password: `admin123`
        - Leave client_id and client_secret blank
     4. Click "Execute" and copy the `access_token` from the response.
   - **Authorize:**
     1. Click the "Authorize" button (lock icon) at the top right.
     2. In the popup, enter:
        ```
        - username: `admin`
        - password: `admin123`
        - Leave client_id and client_secret blank
        ```
     3. Click "Authorize" and then "Close".
   - **Access Protected Endpoints:**
     - Now you can use the student endpoints (create, read, update, delete) by clicking "Try it out" and "Execute". The token will be sent automatically.

---

## Dockerized Deployment
 1. **Setup**
 
     - Install Docker Desktop and sign up.<br>
     - Use the same username and password to sign in into hub.docker.com

2. **Docker Image**
   
   This app is already dockerized and available on Docker Hub:<br>
   https://hub.docker.com/r/saimanasreen/fastapi-crud-app
   

3. **Pull the Docker image**
   
   On any host machine with Docker installed:
   ```bash
   docker pull saimanasreen/fastapi-crud-app
   ```

5. **Run the Docker Container**
   ```bash
   docker run -p 8000:8000 saimanasreen/fastapi-crud-app
   ```
   The app will be accessible at http://localhost:8000/docs

   **Dockerfile Used**
   ```dockerfile
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
   
   **API Documentation**
   
   - Once running (locally or via Docker), access the auto-generated Swagger UI:<br>
   http://localhost:8000/docs







