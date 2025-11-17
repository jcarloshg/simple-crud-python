# 🚀 Simple CRUD Python (FastAPI)

## 📋 Index

1. [🔍 Overview](#overview)
   - [🏗️ Project Structure](#project-structure)
   - [⚡ Technology Stack](#-technology-stack)
2. [⚙️ Setup](#setup)
   - [📋 Prerequisites](#prerequisites)
   - [💾 Installation](#installation)
3. [🚀 Running the App](#running-the-app)
   - [📖 Access Interactive Documentation](#access-interactive-documentation)
4. [🔌 API Endpoints](#api-endpoints)
   - [🏠 GET `/`](#get-)
   - [📄 GET `/items`](#get-items)
   - [➕ POST `/items`](#post-items)
   - [📝 Example Requests](#example-requests)
5. [🧪 Testing](#testing)
   - [📊 Test Coverage](#test-coverage)
6. [🏛️ Architecture & Design Patterns](#architecture--design-patterns)
   - [🎯 Custom Response Pattern](#custom-response-pattern)
   - [🧩 Modular Structure](#modular-structure)
   - [⚠️ Error Handling](#error-handling)
7. [🔧 Development Notes](#development-notes)
   - [💾 In-Memory Storage](#in-memory-storage)
   - [🚀 Future Enhancements](#future-enhancements)
8. [🔄 CI/CD Pipeline](#cicd-pipeline)
   - [🧪 CI Pipeline (Testing)](#ci-pipeline-testing)
   - [🚀 CD Pipeline (Deployment)](#cd-pipeline-deployment)
   - [✨ Benefits](#benefits)
9. [👨‍💻 Author](#author)
10. [📄 License](#license)

## 🔍 Overview

A minimal CRUD API built with FastAPI. CI/CD pipelines are implemented via GitHub Actions for automated testing and deployment.

- 💾 In-memory storage for demonstration and development
- 🔒 Pydantic models for robust request and response validation
- 🏗️ Clean architecture principles with clear separation of concerns
- 🎯 Consistent API output via a custom response wrapper
- ➕ Create items with UUID and message validation
- 📄 Retrieve all items with error handling
- 🎁 Custom response wrapper for consistent API responses
- ✅ Pydantic validation with descriptive error messages
- 🧪 Acceptance tests with pytest

### 🏗️ Project Structure

```
simple-crud-python/
├── main.py                          # FastAPI app entry point
├── requirements.txt                 # Python dependencies
├── pytest.ini                       # Pytest configuration
├── src/
│   └── app/
│       ├── create_item/
│       │   └── create_item.py       # POST /items endpoint handler
│       ├── get_all/
│       │   └── get_all.py           # GET /items endpoint handler
│       └── shared/
│           ├── domain/
│           │   └── custom_response.py  # Custom response wrapper
│           └── infra/
│               └── persist/
│                   └── in_memory/
│                       └── item.py  # In-memory storage list
├── tests/
│   └── acceptance/
│       ├── test_create_item.py      # Create item tests
│       └── test_get_all.py          # Get all items tests
└── docs/
    ├── create.http                  # Valid create item request
    ├── create.bad.http              # Invalid create item request
    └── get_all.http                 # Get all items request
```

### ⚡ Technology Stack

#### Technologies

- 🏗️ Clean architecture with 🏛️ Domain Driven Design
- 🔄 CI/CD with 🤖 GitHub Actions
- 🧪 Acceptance Test

#### Packages Python

- **FastAPI 0.121.2**: 🚀 Modern, fast web framework for building APIs
- **Pydantic 2.12.4**: 🔒 Data validation using Python type annotations
- **Uvicorn 0.38.0**: ⚡ Lightning-fast ASGI server
- **Pytest 9.0.1**: 🧪 Testing framework
- **HTTPX 0.28.1**: 🌐 HTTP client for testing

## ⚙️ Setup

### 📋 Prerequisites

- 🐍 Python 3.8 or higher
- 📦 pip (Python package installer)

### 💾 Installation

1. 📥 Clone the repository:

   ```sh
   git clone <repo-url>
   cd simple-crud-python
   ```

2. 🔧 Create and activate a virtual environment:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. 📦 Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## 🚀 Running the App

Start the FastAPI server with Uvicorn:

```sh
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

#### 📖 Access Interactive Documentation

- **Swagger UI**: 📊 http://127.0.0.1:8000/docs
- **ReDoc**: 📖 http://127.0.0.1:8000/redoc

## 🔌 API Endpoints

### 🏠 GET `/`

**Description**: 👋 Root endpoint returning a welcome message.

**Response**:

```json
"Hello, this is the main endpoint of the API v2"
```

### 📄 GET `/items`

**Description**: 📋 Retrieve all items from in-memory storage.

**Response**:

```json
{
  "message": "Items retrieved successfully",
  "is_success": true,
  "data": [
    {
      "uuid": "a3a19c23-4e64-4fe6-8028-9163a61ea6ea",
      "message": "Sample Hello Word!"
    }
  ]
}
```

### ➕ POST `/items`

**Description**: ✨ Create a new item with validation.

**Request Body**:

```json
{
  "uuid": "a3a19c23-4e64-4fe6-8028-9163a61ea6ea",
  "message": "Sample Hello Word!"
}
```

**Validation Rules**:

- 🆔 `uuid`: Must be a valid UUID4 format
- 💬 `message`: String between 10 and 255 characters

**Success Response** (200):

```json
{
  "message": "Item created successfully",
  "is_success": true,
  "data": {
    "uuid": "a3a19c23-4e64-4fe6-8028-9163a61ea6ea",
    "message": "Sample Hello Word!"
  }
}
```

**Error Response** (200 with error message):

```json
{
  "message": "String should have at least 10 characters",
  "is_success": true,
  "data": null
}
```

### 📝 Example Requests

Sample HTTP request files are available in the `docs/` folder:

#### ✅ Create Item (Valid)

```http
POST http://127.0.0.1:8000/items
Content-Type: application/json

{
  "uuid": "a3a19c23-4e64-4fe6-8028-9163a61ea6ea",
  "message": "Sample Hello Word!"
}
```

#### ❌ Create Item (Invalid UUID)

```http
POST http://127.0.0.1:8000/items
Content-Type: application/json

{
  "uuid": "a3a19c23-4e64",
  "message": "Sample Hello Word!"
}
```

#### 📄 Get All Items

```http
GET http://127.0.0.1:8000/items
```

## 🧪 Testing

Run the test suite using pytest:

```sh
pytest
```

Run specific test files:

```sh
pytest tests/acceptance/test_create_item.py
pytest tests/acceptance/test_get_all.py
```

Run with verbose output:

```sh
pytest -v
```

### 📊 Test Coverage

- **test_create_item.py**: 🧪 Tests item creation with valid data
- **test_get_all.py**: 🧪 Tests retrieval of all items

## 🏛️ Architecture & Design Patterns

### 🎯 Custom Response Pattern

All endpoints use a consistent `CustomResponse` class that wraps responses with:

- 💬 `message`: Descriptive message about the operation
- ✅ `is_success`: Boolean indicating success/failure
- 📦 `data`: The actual payload (can be null)

### 🧩 Modular Structure

- 🛤️ **Routers**: Each feature has its own router (APIRouter)
- 🏷️ **Domain Models**: Pydantic models for validation
- 🏗️ **Infrastructure**: Separated persistence layer
- 🧪 **Tests**: Acceptance tests for each endpoint

### ⚠️ Error Handling

- 🔒 Pydantic ValidationError is caught and converted to user-friendly messages
- ⏭️ Invalid items during retrieval are skipped rather than breaking the entire response

## 🔧 Development Notes

### 💾 In-Memory Storage

- 📝 Data is stored in a simple Python list (`items = []`)
- ⏰ Data persists only during the application runtime
- 🔄 Server restart will clear all data
- ⚠️ **Not suitable for production use**

### 🚀 Future Enhancements

- [ ] 🗃️ Add database persistence (PostgreSQL, MongoDB, etc.)
- [ ] ✏️ Implement UPDATE and DELETE operations
- [ ] 🔐 Add authentication and authorization
- [ ] 📄 Implement pagination for GET /items
- [ ] 🔍 Add filtering and sorting capabilities
- [ ] ❌ Implement proper error responses (400, 404, 500)
- [ ] 📊 Add logging and monitoring
- [ ] 🐳 Docker containerization
- [ ] 🚀 CI/CD pipeline

## 🔄 CI/CD Pipeline

This project implements automated Continuous Integration and Continuous Deployment using GitHub Actions.

### 🧪 CI Pipeline (Testing)

**Workflow**: `.github/workflows/ci-pipeline.yml`

**Triggers**:

- 📤 Push to `dev`, `staging`, or `main` branches
- 🔀 Pull requests to `dev`, `staging`, or `main` branches

**Process**:

1. ✅ Checks out the repository code
2. 🐍 Sets up Python 3.12 environment with pip caching
3. ⬆️ Upgrades pip and installs dependencies from `requirements.txt`
4. 🧪 Runs the full test suite using `pytest`

**Purpose**: 🛡️ Ensures code quality by running automated tests on every commit and pull request, preventing broken code from being merged.

### 🚀 CD Pipeline (Deployment)

**Workflow**: `.github/workflows/cd-pipeline.yml`

**Triggers**:

- 📤 Push to `main` branch
- 🔀 Pull requests to `main` branch

**Process**:

1. 🔗 Connects to production server via SSH (using GitHub secrets)
2. 📂 Navigates to deployment directory (`/home/jcarloshg/deploys`)
3. 📥 Pulls latest code from repository (or clones if first deployment)
4. 🔄 Resets to latest `main` branch state
5. 🗑️ Removes old virtual environment and creates a fresh one
6. 📦 Installs all dependencies from `requirements.txt`
7. 🚀 Starts the FastAPI application using `fastapi run`

**Required Secrets**:

- 🏠 `SSH_HOST`: Production server hostname/IP
- 👤 `SSH_USERNAME`: SSH username
- 🔑 `SSH_PASSWORD`: SSH password (optional if using key)
- 🔐 `SSH_KEY`: SSH private key for authentication
- 🚪 `SSH_PORT`: SSH port number

**Purpose**: 🤖 Automates deployment to production, ensuring the live application is always running the latest tested code from the `main` branch.

### ✨ Benefits

- ✅ Automated testing prevents bugs from reaching production
- ✅ Zero-downtime deployment process
- ✅ Consistent deployment environment
- ✅ Version control integration
- ✅ Fast feedback on code changes

## 👨‍💻 Author

jcarloshg

## 📄 License

MIT
