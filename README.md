# Django Product Catalog

This is a Django project that demonstrates a product catalog with the following features:
- Product model with attributes
- Product detail page with stylized descriptions and images
- REST API to list and filter products
- Jinja2 templates for rendering product pages

## Features

1. **Models**:
   - `Product`: Contains name, slug, description, stylized description, and image fields.
   - `ProductAttribute`: Contains name and slug fields.
   - `ProductAttributeValue`: Contains value, and links to Product and ProductAttribute.

2. **Pages**:
   - Product Catalog page: Displays a list of products.
   - Product Detail page: Displays the details of a selected product, including attributes.

3. **API**:
   - List of products.
   - Filter products by any attribute value.

## Setup

### Prerequisites

- Python 3.8+
- Django 3.2+

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Daniil-Pankieiev/Product-Catalog.git
    cd product_catalog
    ```

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    ```
   Activate On macOS and Linux:
   ```bash
   source venv/bin/activate
   ```
   On Windows:
   ```bash
   venv\Scripts\activate
   ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:

   ```bash
   python manage.py makemigrations
   ```

5. **Run migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

### Populate Database with Example Data

To populate the database with example data, run the following management command:

```bash
python manage.py populate_db
```
### Tests
Run tests:
```bash
python manage.py test
```
###  Usage
Viewing Products

Navigate to http://127.0.0.1:8000/ to view the product catalog.
Click on a product to view its details.

API Endpoints

List of products: GET /api/products/

Filter products by attribute value: GET /api/products/?productattributevalue__value=<value>

