# 💰 Finance Tracking Backend (FastAPI + MySQL)

## 🚀 Project Overview

This is a backend system for managing personal financial transactions.
It allows users to track income and expenses, analyze spending patterns, and securely manage data using authentication.

The project is built using **FastAPI**, **MySQL**, and **JWT Authentication**, following clean architecture principles.

---

## ✨ Features

### 🔐 Authentication & Authorization

* User Registration & Login
* JWT-based authentication
* Role-Based Access Control (Admin / Viewer)

---

### 💳 Transaction Management

* Create, Read, Update, Delete (CRUD) transactions
* Each transaction is linked to a specific user
* Secure APIs with authentication

---

### 🔍 Filtering

* Filter transactions by:

  * Type (income / expense)
  * Category (food, salary, etc.)

Example:

```
GET /transactions?type=income&category=salary
```

---

### 📄 Pagination

* Efficient handling of large data
* Supports page & limit

Example:

```
GET /transactions/paginated?page=1&limit=5
```

---

### 📊 Analytics (Advanced Feature 🔥)

* Total income, expenses, and balance
* Category-wise spending analysis
* Monthly financial trends
* Recent transactions

---

## 🏗️ Tech Stack

| Layer      | Technology        |
| ---------- | ----------------- |
| Backend    | FastAPI           |
| Language   | Python            |
| Database   | MySQL             |
| ORM        | SQLAlchemy        |
| Auth       | JWT (python-jose) |
| Validation | Pydantic          |
| Server     | Uvicorn           |

---

## 📁 Project Structure

```
finance_app/
│
├── models/            # Database models
├── schemas/           # Pydantic schemas
├── routes/            # API routes
├── services/          # Business logic
├── auth/              # Authentication & dependencies
├── database.py        # DB connection
├── main.py            # Entry point
├── .env               # Environment variables
└── README.md
```

---

## ⚙️ Setup Instructions

### 🔹 1. Clone the repository

```
git clone <your-repo-link>
cd finance_app
```

---

### 🔹 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

---

### 🔹 3. Install Dependencies

```
pip install fastapi uvicorn sqlalchemy pymysql python-dotenv
pip install bcrypt==4.0.1 passlib[bcrypt]==1.7.4
pip install python-jose email-validator cryptography
```

---

### 🔹 4. Configure Environment Variables

Create `.env` file:

```
DATABASE_URL=mysql+pymysql://root:yourpassword@localhost/finance_db
SECRET_KEY=your_secret_key
```

---

### 🔹 5. Create Database

Run in MySQL:

```
CREATE DATABASE finance_db;
```

---

### 🔹 6. Run Server

```
uvicorn main:app --reload
```

---

### 🔹 7. Open Swagger Docs

```
http://127.0.0.1:8000/docs
```

---

## 🔑 API Endpoints

### 👤 Users

* `POST /users/register` → Register user
* `POST /users/login` → Login & get JWT token

---

### 💳 Transactions

* `POST /transactions/` → Create transaction (Admin only)
* `GET /transactions/` → Get transactions (with filtering)
* `PUT /transactions/{id}` → Update transaction (Admin)
* `DELETE /transactions/{id}` → Delete transaction (Admin)
* `GET /transactions/paginated` → Paginated results

---

### 📊 Analytics

* `GET /analytics/summary` → Income, expense, balance
* `GET /analytics/category` → Category-wise analysis
* `GET /analytics/monthly` → Monthly trends
* `GET /analytics/recent` → Recent transactions

---

## 🔐 Authentication Usage

1. Login using `/users/login`
2. Copy `access_token`
3. Click **Authorize 🔒** in Swagger
4. Paste token

---

## 🧠 Key Concepts Implemented

* Clean Architecture (routes, services, models separation)
* JWT Authentication
* Role-Based Access Control (RBAC)
* SQL Aggregation (SUM, GROUP BY)
* Filtering & Pagination
* Error Handling & Validation

---

## 💡 Challenges Solved

* bcrypt dependency conflict
* MySQL authentication issues
* JWT integration with Swagger
* Database schema creation
* Input validation using Pydantic

---

## 🎯 Future Enhancements

* Docker Deployment
* CSV Export
* Frontend Integration
* Cloud Deployment (AWS/GCP)

---

## 🏆 Conclusion

This project demonstrates a **real-world backend system** with authentication, database integration, analytics, and scalable API design.

---

## 👨‍💻 Author

**Sasi Kumar Reddy**
