## Exercise 2: Basic FastAPI CRUD APP
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

## 📁 Project Structure:

|--FastAPI_CRUD_APP/<br>
  ├── main.py<br>
  ├── requirements.txt<br>
  ├── venv/<br>
  └── README.md<br>

## 🛠️ Setup Instructions:
1. **Clone the repository**  
   ```bash
   git clone https://github.com/saimanasreen001/FastAPI_CRUD_APP.git
   cd FastAPI_CRUD_APP

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
7. **Test the API**
   ```bash
   Open http://127.0.0.1:8000/docs for the Swagger UI.
   ```





