# Social Media Web Application (Django)

This is a basic social media web application built using **Django** as part of my project submission.

## 🔹 Features Implemented
- User Authentication (Signup, Login, Logout)
- User Profiles
- Create Posts
- View Posts Feed
- Like Posts
- Follow / Unfollow Users

## 🔹 Tech Stack
- Python
- Django
- HTML, CSS
- SQLite (default Django database)

## 🔹 Project Flow
1. User can sign up or log in
2. After login, user is redirected to feed
3. Users can create posts
4. Users can like posts
5. Users can follow other users
6. Feed shows posts from users

## 🔹 How to Run the Project Locally

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Then open:
http://127.0.0.1:8000/


 Notes

Virtual environment (venv) is not included

Database file is not included

