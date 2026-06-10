# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a small REST API using the FastAPI framework. Students will build endpoints to create, read, and list resources and run the app locally.

## 📝 Tasks

### 🛠️ Implement the API

#### Description
Create a FastAPI application that exposes endpoints to manage `items` (in-memory):

- `GET /items` — list all items
- `POST /items` — create a new item
- `GET /items/{id}` — get an item by id

#### Requirements
Completed program should:

- Provide the listed endpoints and use JSON for input/output.
- Validate input and return appropriate HTTP status codes (400/404 where applicable).
- Use Pydantic models for request/response validation.
- Include a `starter-code.py` that contains a minimal FastAPI app scaffold.

## 🔎 Example Requests

Create an item:

```bash
curl -X POST "http://localhost:8000/items" -H "Content-Type: application/json" -d '{"id":1,"name":"Example","description":"Sample item"}'
```

List items:

```bash
curl "http://localhost:8000/items"
```

Get item by id:

```bash
curl "http://localhost:8000/items/1"
```

## 🧾 Starter files

- `starter-code.py` — Minimal FastAPI app scaffold
- `requirements.txt` — Dependencies to install (`fastapi`, `uvicorn`)

## ✅ Evaluation checklist

- The API runs locally with `uvicorn starter-code:app --reload`.
- Endpoints return correct status codes and JSON payloads.
- Handles duplicate IDs and missing resources gracefully.

## 💡 Hints

- Use `from pydantic import BaseModel` to define request/response models.
- Track items in a simple list for this assignment (no database required).

**Skills practiced:** Web APIs, JSON, request validation, basic server development with FastAPI
