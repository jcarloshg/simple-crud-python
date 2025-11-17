# Simple CRUD Python (FastAPI)

A minimal CRUD API built with FastAPI, featuring:

- In-memory storage for demonstration and development
- Pydantic models for robust request and response validation
- Clean architecture principles with clear separation of concerns
- Consistent API output via a custom response wrapper
- Comprehensive acceptance tests using pytest

## Features

- ✅ Create items with UUID and message validation
- ✅ Retrieve all items with error handling
- ✅ Custom response wrapper for consistent API responses
- ✅ Pydantic validation with descriptive error messages
- ✅ In-memory storage (development/demo purposes)
- ✅ Acceptance tests with pytest
- ✅ Clean architecture with modular structure

## Project Structure

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

## Technology Stack

- **FastAPI 0.121.2**: Modern, fast web framework for building APIs
- **Pydantic 2.12.4**: Data validation using Python type annotations
- **Uvicorn 0.38.0**: Lightning-fast ASGI server
- **Pytest 9.0.1**: Testing framework
- **HTTPX 0.28.1**: HTTP client for testing

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

   ```sh
   git clone <repo-url>
   cd simple-crud-python
   ```

2. Create and activate a virtual environment:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the App

Start the FastAPI server with Uvicorn:

```sh
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### Access Interactive Documentation

- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## API Endpoints

### GET `/`

**Description**: Root endpoint returning a welcome message.

**Response**:

```json
"Hello, this is the main endpoint of the API v2"
```

### GET `/items`

**Description**: Retrieve all items from in-memory storage.

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

### POST `/items`

**Description**: Create a new item with validation.

**Request Body**:

```json
{
  "uuid": "a3a19c23-4e64-4fe6-8028-9163a61ea6ea",
  "message": "Sample Hello Word!"
}
```

**Validation Rules**:

- `uuid`: Must be a valid UUID4 format
- `message`: String between 10 and 255 characters

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

## Testing

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

### Test Coverage

- **test_create_item.py**: Tests item creation with valid data
- **test_get_all.py**: Tests retrieval of all items

## Example Requests

Sample HTTP request files are available in the `docs/` folder:

### Create Item (Valid)

```http
POST http://127.0.0.1:8000/items
Content-Type: application/json

{
  "uuid": "a3a19c23-4e64-4fe6-8028-9163a61ea6ea",
  "message": "Sample Hello Word!"
}
```

### Create Item (Invalid UUID)

```http
POST http://127.0.0.1:8000/items
Content-Type: application/json

{
  "uuid": "a3a19c23-4e64",
  "message": "Sample Hello Word!"
}
```

### Get All Items

```http
GET http://127.0.0.1:8000/items
```

## Architecture & Design Patterns

### Custom Response Pattern

All endpoints use a consistent `CustomResponse` class that wraps responses with:

- `message`: Descriptive message about the operation
- `is_success`: Boolean indicating success/failure
- `data`: The actual payload (can be null)

### Modular Structure

- **Routers**: Each feature has its own router (APIRouter)
- **Domain Models**: Pydantic models for validation
- **Infrastructure**: Separated persistence layer
- **Tests**: Acceptance tests for each endpoint

### Error Handling

- Pydantic ValidationError is caught and converted to user-friendly messages
- Invalid items during retrieval are skipped rather than breaking the entire response

## Development Notes

### In-Memory Storage

- Data is stored in a simple Python list (`items = []`)
- Data persists only during the application runtime
- Server restart will clear all data
- **Not suitable for production use**

### Future Enhancements

- [ ] Add database persistence (PostgreSQL, MongoDB, etc.)
- [ ] Implement UPDATE and DELETE operations
- [ ] Add authentication and authorization
- [ ] Implement pagination for GET /items
- [ ] Add filtering and sorting capabilities
- [ ] Implement proper error responses (400, 404, 500)
- [ ] Add logging and monitoring
- [ ] Docker containerization
- [ ] CI/CD pipeline

## Troubleshooting

### Port Already in Use

If port 8000 is already in use, specify a different port:

```sh
uvicorn main:app --reload --port 8001
```

### Module Not Found

Ensure you're in the correct directory and virtual environment is activated:

```sh
pwd  # Should show /path/to/simple-crud-python
which python  # Should show .venv/bin/python
```

### Import Errors

The project uses absolute imports from `src/`. Ensure you run commands from the project root.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT

## Author

jcarloshg
