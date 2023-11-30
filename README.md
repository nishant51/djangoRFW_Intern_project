# Django Backend Application

This Django backend application provides API endpoints for managing tasks with basic CRUD operations.

## Setup and Run Instructions

Follow these steps to set up and run the Django backend application locally.

### Prerequisites

- [Python](https://www.python.org/downloads/) installed
- [pip](https://pip.pypa.io/en/stable/installation/) installed

### Clone the Repository

```bash
git https://github.com/nishant51/djangoRFW_Intern_project.git
cd djangoRFW_Intern_project
```
### Create and Activate Virtual Environment (venv)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python -m venv venv
source venv/bin/activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```

### Database Setup
Edit the DATABASES configuration in myproject/settings.py to match your database setup.

Example using SQLite:
```bash
python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

```


### Run Migrations
```bash
python manage.py migrate 
```
### Create Superuser (Optional)

Create an admin superuser to access the Django admin interface:
```bash
python manage.py createsuperuser
```
## Run the Application
```bash
python manage.py runserver
```
The application will be available at http://localhost:8000/.

### API Documentation
 the documentation link is given here : click here


### Testing
```bash
python manage.py test app.tests
```
### Additional Notes

# 1) Make sure to configure ALLOWED_HOSTS in myproject/settings.py for production deployment.

# 2) For secure authentication, obtain a JWT token by sending a POST request to the authentication endpoint (/api/token/).

# 3) Additional customization can be done in app/models.py, app/serializers.py, and app/views.py.







