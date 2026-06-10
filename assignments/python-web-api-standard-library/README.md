# 📘 Assignment: Beginner Web APIs with Python Standard Library

## 🎯 Objective

Build a simple JSON HTTP service using Python's standard library to introduce API concepts without external dependencies.

## 📝 Tasks

### 🛠️ Implement the API server

#### Description
Create a small HTTP server using `http.server` that responds to GET requests with JSON data.

#### Requirements
Completed program should:

- Use `http.server` to handle requests on a local port.
- Serve JSON responses for at least one endpoint, such as `/status` or `/items`.
- Return the correct `Content-Type: application/json` header.
- Handle invalid paths with a `404` response.

### 🛠️ Add sample data handling

#### Description
Extend the server so it returns a list of items or status information in JSON form.

#### Requirements
Completed program should:

- Return a JSON array or object with sample data.
- Include at least one field for `name` or `status`.
- Keep the implementation simple and easy to run.

## 🔎 Example Request / Response

Request:

```bash
curl http://localhost:8000/status
```

Response:

```json
{
  "status": "ok",
  "message": "Server is running"
}
```

## 🧾 Starter files

- `starter-code.py` — Minimal HTTP server scaffold

## ✅ Evaluation checklist

- The server starts locally and listens on a port.
- JSON responses are returned with the correct headers.
- Invalid routes return a `404` status.

## 💡 Hints

- Use `from http.server import BaseHTTPRequestHandler, HTTPServer`.
- Use `json.dumps()` to serialize Python data.

**Skills practiced:** HTTP basics, JSON serialization, Python standard library, simple server implementation
