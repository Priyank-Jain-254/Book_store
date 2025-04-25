HEAD
# 📚 Bookstore Management System

A Django web app for browsing, adding to cart, and managing books.

## 🔧 Tech Stack
- Python 3.11.8
- Django
- Docker
- Jenkins
- Manual HTML Forms (no Django forms)
- Class-Based Views (CBVs only)

## 🚀 How to Run

###  With Docker

-----bash----

docker-compose up --build

### Without Docker
------bash--------

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

