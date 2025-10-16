🌱 Plant Management System
Project Overview

Plant Management is a simple web app made with Django.
It helps people who love plants to add, edit, delete, and view plants online.
Each plant has a name, price, life cycle, age, and photo.
The goal is to make it easy for users to keep their plant list organized and share it with others.

🎯 Purpose

The project was created to help users (gardeners, students, or shop owners) save and manage plant information online in one place.
It gives a friendly design that works well on both computers and phones.

🌿 Main Features
🔐 User System

Sign Up / Log In / Log Out using Django’s built-in system.

Each user can manage their own plants only.

🌼 Plant Management

Add Plant: Add name, price, age, life cycle, and upload an image.

View Plants: See all plants added by users.

Edit or Delete: Change or remove your own plants.

Form Design: Simple and clean with custom CSS.

🖼️ Images

Upload real plant photos.

Photos are shown on the website dynamically.

🔍 Easy Navigation

All pages are made with Django templates.

Home page shows all plants.

Details page shows full information for one plant.

Works well on mobile screens.

🧱 Tech Stack
Part	Technology
Backend	Django (Python)
Frontend	HTML, CSS, JavaScript
Database	SQLite
Authentication	Django built-in system
Image Upload	Django ImageField
🧩 Database Design (ERD)
erDiagram
    USERS {
        int id PK
        varchar name
        varchar email
        varchar password
        int phone_number
    }

    PLANTS {
        int plan_id PK
        varchar name
        varchar category
        varchar life_cycle
        int price
        timestamp old
    }

    CATEGORIES {
        int plant_id FK
        varchar trees
        varchar shrubs
        varchar herbs
        varchar climbing
        varchar creeping
    }

    ORDERS {
        int order_id PK
        int total_amount
        varchar order_status
        timestamp order_date
        int user_id FK
    }

    ORDER_ITEMS {
        int id PK
        varchar inside_the_order
        int number_of_seedlings
        int order_id FK
        int plant_id FK
    }

    USERS ||--o{ ORDERS : places
    ORDERS ||--|{ ORDER_ITEMS : contains
    PLANTS ||--|{ ORDER_ITEMS : listed_in
    PLANTS ||--|| CATEGORIES : classified_as

👥 User Stories
Authentication

As a visitor, I can view all plants.

As a visitor, I need to log in before adding or editing a plant.

As a registered user, I can log in and manage my own plants.

As a registered user, I can log out safely.

Plants

I can add new plants with name, price, and image.

I can edit or delete only my own plants.

I can see all plants and their details easily.

Interface

The website has a clean and easy design.

Messages appear after adding or deleting a plant.

⚙️ Installation & Setup
1️⃣ Clone Repository
git clone https://github.com/yourusername/Plant-Management.git
cd Plant-Management

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser (optional)
python manage.py createsuperuser

6️⃣ Start the Server
python manage.py runserver


Visit the app on: http://127.0.0.1:8000/

📸 Example Pages
Page	Description
🏠 Home	Shows all plants
➕ Add Plant	Form to add a new plant
🧾 Details	View full plant info
✏️ Edit/Delete	Manage your own plants
🔐 Login/Sign Up	User system
🚀 Future Ideas

Add a search bar to find plants quickly.

Add a category filter (trees, herbs, etc.).

Add comments or likes for plants.

Make a simple order system for selling plants.

💡 Goal

To build a complete Django web app with models, views, templates, CRUD actions, and authentication — using clear design and easy user experience.