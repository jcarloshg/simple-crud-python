# Simple CRUD Python (FastAPI)

A minimal CRUD API built with FastAPI, using in-memory storage and Pydantic for validation.

## Features

- Create items with UUID and message
- Get all items
- Basic validation and custom response

## Project Structure

- `main.py`: FastAPI app entry point
- `src/app/create_item/create_item.py`: POST /items endpoint
- `src/app/shared/domain/custom_response.py`: Custom response class
- `src/app/shared/infra/persist/in_memory/item.py`: In-memory item list
- `docs/`: HTTP request samples

## Setup

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

## API Endpoints

- `GET /` — Hello World
- `GET /items` — List all items
- `POST /items` — Create a new item
- `GET /items/{item_id}` — Example endpoint (not connected to storage)

## Example Requests

See the `docs/` folder for sample HTTP requests.

## Notes

- Data is stored in-memory and will reset on server restart.
- For production, replace with a persistent database.

## License

MIT
