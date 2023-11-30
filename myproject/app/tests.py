from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth.models import User

class TaskAPITestCase(TestCase):

    def setUp(self):                     #This method is called before each test case. It sets up the test client, creates a task object for testing, and defines URLs for the test.
        self.client = APIClient()
        self.task_data = {
            "title": "Test Task",
            "body": "Test description",
            "status": "pending"
        }
        self.task = Task.objects.create(**self.task_data)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.task_url = f'/api/task-update/{self.task.id}/'
        self.api_overview_url = '/api/api-overview/'


    def test_task_list(self):                             #Tests the /api/task-list/ endpoint to ensure it returns the expected list of tasks.
        response = self.client.get('/api/task-list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one task is created in setUp

              
   #Tests the /api/task-create/ endpoint to ensure it creates a new task.
    def test_task_create(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/api/task-create/', self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)


    def test_task_update(self):                 #Tests the /api/task-update/<str:pk>/ endpoint to ensure it updates an existing task
        updated_data = {
            "title": "Updated Test Task",
            "body": "Updated test description",
            "status": "completed"
        }
        response = self.client.post(self.task_url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, "Updated Test Task")
        self.assertEqual(self.task.body, "Updated test description")
        self.assertEqual(self.task.status, "completed")

    def get_auth_token(self):
        response = self.client.post('/api/token/', {'username': 'testuser', 'password': 'testpassword'})
        return response.data['access']


                      

