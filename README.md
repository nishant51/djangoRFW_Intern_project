# Django Backend Application

This Django backend application provides API endpoints for managing tasks with basic CRUD operations with jwt validation,error_Status and few unit test .

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
python manage.py makemigrations
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

 the documentation link is given here : [click here](https://github.com/nishant51/djangoRFW_Intern_project/blob/main/Task%20Management%20API%20Documentation.docx.pdf)


### Testing

```bash
python manage.py test app.tests
```

## Testing with Postman

#### Obtain JWT Token
Send a POST request to the authentication endpoint (/api/token/) 
with your username and password to obtain a JWT token. Use the token for subsequent authenticated requests.

Example:

```bash
curl -X POST -d "username=<your_username>&password=<your_password>" http://localhost:8000/api/token/
# Include the obtained token in the Authorization header for authenticated requests:

Authorization: Bearer <your_access_token>
# Testing Endpoints with Postman
```

#### Use Postman to test the API endpoints:

  1) Import the provided Postman collection (postman_collection.json) into your Postman workspace.
  2) Update the environment variables with your local server information and token.
  3) Generate API Documentation with Postman

#### Open Postman.
 1) Create a new workspace and import the collection (postman_collection.json).
 2) Click on "API" in the left sidebar and select "API Documentation."
 3)  Postman will generate API documentation based on your collection.

## Additional Notes

 1) Make sure to configure ALLOWED_HOSTS in myproject/settings.py for production deployment.

 2) For secure authentication, obtain a JWT token by sending a POST request to the authentication endpoint (/api/token/).

 3) Additional customization can be done in app/models.py, app/serializers.py, and app/views.py.







