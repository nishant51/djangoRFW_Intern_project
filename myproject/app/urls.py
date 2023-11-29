from django.urls import path
from django.contrib import admin
from . import views
from django.conf import settings
from .views import authenticated_endpoint, obtain_token

urlpatterns = [
    path('token/', obtain_token, name='token-obtain'),
    path('authenticated/', authenticated_endpoint, name='authenticated-endpoint'),
    path('',views.apioverview ,name ='apioverview'),
    path('task-list/',views.Tasklist,name = 'tasklist'),
    path('task-create/',views.Taskcreate,name = 'taskcreate'),
    path('task-update/<str:pk>/',views.Taskupdate,name = 'taskupdate'),
    path('task-update/<str:pk>/',views.Taskupdate,name = 'taskupdate'),
    path('task-delete/<str:pk>/', views.taskdelete,name='task-delete'),

]
