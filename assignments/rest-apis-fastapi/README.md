# 📘 Assignment: Building REST APIs with FastAPI Framework

## 🎯 Objective

Build REST APIs using the FastAPI framework in Python, implementing CRUD operations and proper request/response handling.

**Skills practiced:** API development, HTTP methods, request validation, response models, asynchronous programming

## 📝 Tasks

### 🛠️ Set Up Basic FastAPI Application

#### Description

Create a basic FastAPI application with a root endpoint that returns a welcome message.

#### Requirements

Completed program should:

- Import FastAPI and create an app instance
- Define a GET endpoint at "/" that returns a JSON response with a welcome message
- Run the application using uvicorn server

### 🛠️ Implement CRUD Endpoints for Items

#### Description

Create REST API endpoints for managing a collection of items with full CRUD operations.

#### Requirements

Completed program should:

- Define a Pydantic model for Item with fields: id, name, description, price
- Implement GET /items to retrieve all items
- Implement POST /items to create a new item
- Implement GET /items/{item_id} to retrieve a specific item
- Implement PUT /items/{item_id} to update an item
- Implement DELETE /items/{item_id} to delete an item
- Use appropriate HTTP status codes
- Handle cases where item is not found

### 🛠️ Add Request Validation and Response Models

#### Description

Enhance the API with proper request validation, response models, and error handling.

#### Requirements

Completed program should:

- Use Pydantic models for request bodies and responses
- Add validation for item fields (e.g., price must be positive)
- Implement custom exception handlers for validation errors
- Add API documentation using FastAPI's automatic docs
- Include example requests and responses in the documentation