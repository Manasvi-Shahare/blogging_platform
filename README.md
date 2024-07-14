# RESTful Blog API Platform

This project implements a RESTful API for a simple blogging platform using Flask. The API supports user authentication and CRUD operations on blog posts.

## Features

- User Signup and Login with password hashing
- Authentication using HTTP Basic Auth
- CRUD operations for blog posts
- SQLAlchemy for ORM
- Flask-Migrate for database migrations
- Unit tests for critical functionalities

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Manasvi-Shahare/blog_api.git
   cd blog_api

2. **modify the database url of your config.py file:**
   ```bash
   SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:port/blog_db'
   ```
   replace the username, password and port with your postgresql database credentials

3. **Initialize the database:**
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade

4. **Run the application:**
   ```bash
   flask run

## Usage
Use tools like Postman or cURL to interact with the API. Below are some example requests.

### Endpoints

#### User Authentication
1. Signup: POST http://127.0.0.1:5000/signup
   
   JSON request body:
   ```bash
   {
     "username": "testuser",
     "password": "testpassword"
   }
   ```
2. Login: POST http://127.0.0.1:5000/login
   
   JSON request body:
   ```bash
   {
     "username": "testuser",
     "password": "testpassword"
   }
   ```
### Blog Posts
1. Create a Post: POST http://127.0.0.1:5000/posts
   
   Headers: Authorization: Basic Auth (username:"testuser" password:"testpassword")
   
   JSON request body:
   ```bash
   {
     "title": "New Post",
     "content": "This is the content of the new post."
   }
   ```
3. Get All Posts: GET http://127.0.0.1:5000/posts

4. Get a Post by ID: GET http://127.0.0.1:5000/posts/1
   
5. Update a Post: PUT http://127.0.0.1:5000/posts/1
  
   Headers: Authorization: Basic Auth (username:"testuser" password:"testpassword")
   
   JSON request body:
   ```bash
   {
     "title": "Updated Post",
     "content": "This is the updated content of the existing post."
   }
   ```
7. Delete a Post: DELETE http://127.0.0.1:5000/posts/1
   
   Headers: Authorization: Basic Auth (username:"testuser" password:"testpassword")

## Testing
Run the unit tests using the following command:
```bash
python -m unittest discover -s tests
```

## Design Decisions
1. Flask Framework: Chosen for its simplicity and ease of use in building RESTful APIs.
2. SQLAlchemy: Provides a robust ORM for interacting with the database.
3. Flask-Migrate: Manages database migrations, making it easy to handle schema changes.
4. HTTP Basic Auth: Simple authentication mechanism suitable for a basic API.

## Trade-offs
1. Basic Auth vs. Token Auth: Basic Auth was used for simplicity. Token-based authentication (e.g., JWT) would be more secure and scalable for larger applications.
2. Unittest vs. Pytest: Unittest is built-in testing framework in Python, straightforward and integrates well with existing code. However, it might lack some advanced features. Pytest is powerful testing framework with advanced features like fixtures and parameterized testing. However, it might require additional learning and setup.

## Improvements
1. Token-based Authentication: Implement JWT for more secure and scalable authentication.
2. Rate Limiting: Protect the API from abuse by implementing rate limiting.
3. Pagination: Add pagination to the GET /posts endpoint to handle large datasets efficiently.
4. Validation: Add more comprehensive request validation and error handling.
5. Deployment: Containerize the application using Docker for easy deployment and scaling.

## API Documentation

### Base URL
All API endpoints are relative to:
```bash
curl http://127.0.0.1:5000
```

### Example cURL Commands
1. Signup:
   ```bash
   curl -X POST http://127.0.0.1:5000/signup -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}'
   ```
2. Login:
   ```bash
   curl -X POST http://127.0.0.1:5000/login -H "Content-Type: application/json" -d '{"username": "testuser", "password": "testpassword"}'
   ```
3. Create a Post:
   ```bash
   curl -X POST http://127.0.0.1:5000/posts -H "Content-Type: application/json" -H "Authorization: Basic $(echo -n 'testuser:testpassword' | base64)" -d '{"title": "New Post", "content": "This is the content of the new post."}'
   ```
4. Get All Posts:
   ```bash
   curl -X GET http://127.0.0.1:5000/posts
   ```
5. Get a Post by ID:
   ```bash
   curl -X GET http://127.0.0.1:5000/posts/1
   ```
6. Update a Post:
   ```bash
   curl -X PUT http://127.0.0.1:5000/posts/1 -H "Content-Type: application/json" -H "Authorization: Basic $(echo -n 'testuser:testpassword' | base64)" -d '{"title": "Updated Post", "content": "Updated content."}'
   ```
7. Delete a Post:
   ```bash
   curl -X DELETE http://127.0.0.1:5000/posts/1 -H "Authorization: Basic $(echo -n 'testuser:testpassword' | base64)"
   ```
