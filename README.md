# Blog

Create a Virtual Environment using Django

Make sure your project directory structure looks like this:

Step 1 :
# Create project directory
    mkdir django_blog
    cd django_blog

# Create virtual environment
    python -m venv blog_env

# Activate virtual environment
# Windows:
    blog_env\Scripts\activate
# macOS/Linux:
    source blog_env/bin/activate

# Install Django
    pip install django pillow

# Create Django project
    django-admin startproject blog_project .

# Create blog app
    python manage.py startapp blog

# Create accounts app for authentication
    python manage.py startapp accounts




2. Structure of our blog project 
django_blog/
├── blog_project/
│   ├── _init_.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── blog/
│   ├── _init_.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── accounts/
│   ├── _init_.py
│   ├── admin.py
│   ├── apps.py
│   ├── urls.py
│   └── views.py
├── templates/
│   ├── base.html
│   ├── blog/
│   │   ├── home.html
│   │   ├── post_detail.html
│   │   ├── create_post.html
│   │   └── user_posts.html
│   └── registration/
│       ├── login.html
│       └── register.html
├── static/
├── media/
└── manage.py

Step 3

Key Features of the Registration System:
    1.User Registration: Complete signup form with username and password
    2.User Login: Secure login with error handling
    3.Form Validation: Built-in Django validation with Bootstrap styling
    4.Responsive Design: Mobile-friendly forms
    5.Error Messages: Clear feedback for validation errors
    6.Navigation: Easy switching between login and registration
    7.Auto-redirect: Users are redirected to home page after successful registration/login
    8.Setup Steps Reminder:
    9.Create the directory structure
    10.Copy all the code files
 Run migrations:

    python manage.py makemigrations
    python manage.py migrate
    
Create a superuser:

    python manage.py createsuperuser
    
Run the server:

    python manage.py runserver
