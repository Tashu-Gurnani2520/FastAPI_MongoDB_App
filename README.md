# Ecommerce Backend with FastAPI and MongoDB

This project implements an ecommerce backend using FastAPI for building APIs and MongoDB as the database. The backend includes features like user authentication, product management, cart management, and order creation.

# Features

## User Authentication
Signup: Create a new user.
Login: Authenticate users using credentials.

## Product Management
Add Product: Admins can add new products to the catalog.
Get Products: View all available products in the store.

## Cart Management
Add Item to Cart: Users can add products to their shopping cart.
Get Cart: Retrieve items in the user's cart.

## Order Creation
Create Order: Users can place orders for the items in their cart.

# Technologies
## FastAPI: 
A modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints. It is built on top of Starlette for the web parts and Pydantic for data validation.

## MongoDB: 
A NoSQL document-based database that stores data in flexible, JSON-like format. It is used here to store user information, products, cart data, and orders.

# Setup

## Prerequisites
Python 3.7+
MongoDB for cloud database.

## Installation

Clone the repository:

```python
git clone https://github.com/Tashu-Gurnani2520/FastAPI_MongoDB_App.git
```

```python
cd ecommerce-backend
```

Create a virtual environment:

```python
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
```

Install the dependencies:
```python
pip install -r requirements.txt
```

Run the application:
```python
uvicorn main:app --reload
```

The API will be available at http://127.0.0.1:8000.

# Connecting to MongoDB
In order to connect your FastAPI application to MongoDB, you will need to have either a local MongoDB instance or a MongoDB Atlas cloud database. Here I have illustrated connecting with cloud database.

(configurations file database.py)

```python
client = MongoClient("mongodb+srv://<username>:<password>@cluster0.mongodb.net/ecommerce_db?retryWrites=true&w=majority")
db = client["ecommerce_db"]
```

Ensure you replace <username> and <password> with your MongoDB credentials.

# Key Components of FastAPI
## FastAPI Application (main.py)
The FastAPI app is the core of your application. It is where the API instance is created, routes are defined, and dependencies are configured. This is where the FastAPI server is initialized, and the various routers for different modules (such as user authentication, product management, etc.) are included to define the API structure.

## Database Models (models.py)
In FastAPI, models represent the structure of the data being stored in the database. MongoDB is used in this project, so the models correspond to the collections in MongoDB. These models define how the data is stored, including the fields and their types. Models are also used for data validation and serialization.

## Pydantic Schemas (schemas.py)
Pydantic schemas are used in FastAPI to define the structure of the data for both request bodies and response bodies. They play a crucial role in data validation, ensuring that the incoming data is in the correct format and meets the expected constraints. Pydantic schemas help FastAPI automatically handle serialization and validation.

Request schemas are used to validate data sent by the client in API requests.
Response schemas define the format of the data sent back in API responses.

## API Endpoints
API endpoints define the routes that the client can interact with. In FastAPI, each endpoint is linked to an HTTP method (GET, POST, PUT, DELETE, etc.) and is associated with a specific path (URL). These endpoints allow clients to interact with the backend to perform operations like creating a user, adding a product, or placing an order. Each endpoint is typically implemented as a function that performs the necessary logic for handling the request.

Once your FastAPI app is running (by using uvicorn), you can access Swagger UI by navigating to:

http://127.0.0.1:8000/docs

# References

FastAPI Documentation
MongoDB Documentation
Uvicorn Documentation


