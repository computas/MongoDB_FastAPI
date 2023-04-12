# Python FastAPI + MongoDB REST API
This is a simple REST API built with Python FastAPI and MongoDB, allowing clients to perform CRUD (create, read, update, delete) operations on a collection of people.

## Requirements
- Python 3.8+ 
- pip (Python package installer)
- MongoDB (either locally or remotely)

## Getting started
1. Clone the repository::
```	
git clone https://github.com/computas/MongoDB_FastAPI.git
```

2. It is recommended to use a virtual environment for this project. Look [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to learn more about virtual environments. To install the required packages, run:
```
pip install -r requirements.txt
```

3. Activate your environment and start the FastAPI server by running:
```
uvicorn main:app --reload
```
The API server will run on http://localhost:8000 or http://127.0.0.1:8000. When using the reload tag, the server will reload automatically when the aplication is updated.

When the server is running, a client can make eiter a GET, POST, PUT or DELETE request to the API. To stop the server, press Ctrl+C.

## API endpoints
The API has the following endpoints:
- **GET /people/**: List all people documents.
- **GET /people/{id}**: Get a single person document by ID.
- **POST /people/**: Create a new person document. This needs a body element with the following format (Note: _id is automatically generated):
```
{
    "name": "John Doe",
    "age": 42,
    "address": "123 Main Street, Anytown, USA"
}
```
- **PUT /people/{id}**: Update a person document by ID. This also needs a body element with the same format as the POST request, but without an _id element.
- **DELETE /people/{id}**: Delete a person document by ID.

## API documentation
The API documentation is available at http://localhost:8000/docs, this opens Swagger UI which is a part of FastAPI. The documentation includes a description of the endpoints, the parameters and the responses. Or you can use [*Postman*](https://www.postman.com/) to test the API.

