# Mini E-commerce Application

This is a mini e-commerce application built with a **Django backend** using the **Django REST Framework (DRF)** and a **Vue.js frontend**. The app features a product catalog where users can view, add, edit, delete and filter products based on availability (in-stock or out-of-stock). The backend provides APIs for managing products, including CRUD operations, and supports pagination for displaying products in batches.

## Features

- **Product Catalog**: View all products and filter them based on their availability (in-stock or out-of-stock).
- **Pagination**: Fetch paginated products with 5 products per page.
- **CRUD Operations**: Create, read, update, and delete products.
- **In-stock filter**: Filter products based on their stock status.
- **Backend**: Django REST Framework for APIs.
- **Frontend**: Vue.js for a dynamic and responsive user interface.
- **Real-time Updates**: The application supports real-time functionalities, ensuring any product changes are reflected immediately.  
- **Responsive Design**: The frontend is designed to adapt seamlessly to various screen sizes, ensuring an optimal user experience on desktop and mobile devices.  


## Getting Started

### Prerequisites

- [Node.js](https://nodejs.org/) (for the frontend)
- [Python](https://www.python.org/) (for the backend)
- [Django](https://www.djangoproject.com/) (for the backend)
- [Django REST Framework](https://www.django-rest-framework.org/) (for the backend)
- [Vue.js](https://vuejs.org/) (for the frontend)

### Project Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/test_technique_tiktakpro.git
```

### Backend Setup

```bash
cd ../backend

# Install dependencies
pip install -r requirements.txt

# Migrate the database
python manage.py migrate


# Start the Django server
python manage.py runserver
```
### Frontend Setup

```bash
# Navigate to the frontend directory
cd ../frontend

# Install dependencies
npm install

# Start the Vue.js development server
npm run serve
```

## Launching Backend Tests

To test the backend functionality, follow these steps:

### 1. Navigate to the `backend` directory: 

   ```bash
   cd backend
   python manage.py test
```
This will execute all the defined unit tests for the backend, including tests for all possible CRUD operations (Create, Read, Update, Delete) and any additional logic implemented for the API endpoints.

Adding Tests
If you wish to add your own tests, create test cases in a tests.py file located in the Django app directory (e.g., app/tests.py)
## API Endpoints

### Base URL +

### 1. **Get Paginated Products**
Fetch a list of products with pagination support.

- **URL:** `/paginated-products/`
- **Method:** `GET`
- **Query Parameters:**
  - `page`: The page number (default is `1`).
  - `page_size`: The number of products per page (default is `5`).
  - `in_stock`: Whether to filter products that are in stock (`true` or `false`).

#### Example Request:
```bash
GET /api/paginated-products/?page=1&page_size=5&in_stock=true
```


### 2. **Get Product by ID**
Retrieve a product by its ID.

- **URL:** `/api/products/{id}/`
- **Method:** `GET`

#### Example Request:
```bash
GET /api/products/1/
```
### 3. **Create a Product**
Create a new product.

- **URL:** `/api/products/`
- **Method:** `POST`
- **Body:**
    - `name: The name of the product.
    - `description: The description of the product.
    - `price: The price of the product.
    - `stock: The stock quantity of the product.

#### Example Request:
```bash
POST /api/products/
```
### 4. **Update Product**
Update a product's details.

- **URL:** `/api/products/{id}/`
- **Method:** `PUT or PATCH`
- **Body:**
    - name: The name of the product.
    - description: The description of the product.
    - price: The price of the product.
    - stock: The stock quantity of the product.

#### Example Request:
```bash
PUT /api/products/1/
```
### 5. **Delete Product**
Delete a product.

- **URL:** `/api/products/{id}/`
- **Method:** `DELETE`

#### Example Request:
```bash
DELETE /api/products/1/
```
### 6. **Get All Products**
Retrieve a list of all products.

- **URL:** `/api/products/`
- **Method:** `GET`


#### Example Request:
```bash
GET /api/products/
```
### 7. **Get All Products in Stock**
Retrieve a list of all products.

- **URL:** `/api/products/in_stock/`
- **Method:** `GET`


#### Example Request:
```bash
GET /api/products/in_stock/
```

## Directory Structure
```bash
test_technique_tiktakpro/
├── backend/               # Django backend
│   ├── app/               # Django app
│   ├── manage.py          # Django management script
│   ├── requirements.txt   # Python dependencies
│   ├── app/views.py       # Views and viewsets for the app
│   └── app/models.py      # Models for the app
├── frontend/              # Vue.js frontend
│   ├── src/               # Vue.js source code
│   ├── package.json       # Node.js dependencies
│   └── public/            # Static files
├── .gitignore             # Git ignore file
└── README.md              # This README file
```
# Developed by ZAGHBIB Moemen for TIKTAK PRO company's technical test.
