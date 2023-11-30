from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from  .models import Task
from .serializers import TaskSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def authenticated_endpoint(request):
    return Response({'message': 'You are authenticated!'})

@api_view(['POST'])
def obtain_token(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if username and password:
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=401)
    else:
        return Response({'error': 'Username and password are required'}, status=400)


#overall overview of the total task that can be performed in this api with their respective apis urls 
@api_view(['GET'])
def apioverview(request):
        api_urls = {
        'obtail_token':'/token/',
        'authenticated_endpoint':'/authenticated/',
        'list':'/task-list/',
        'create':'/task-create/',
        'update ':'/task-update/<str:pk>/',
        'delete':'/task-delete/<str:pk>/',
        }   
        return Response(api_urls)


# performing Read operation and displaying all data stored in database in console
@api_view(['GET'])
def Tasklist(request):
        try:
              tasks = Task.objects.all()
              serializer = TaskSerializer(tasks,many =True)
              return Response(serializer.data)
        except Exception as e:
              return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# performing create operation and adding that data in database 
@api_view(['POST'])
@permission_classes([IsAuthenticated])                       #this decorator is used to make create endpoint secure 
def Taskcreate(request):
    try:                                                            # used try and catch method to handle error and show specific error and success http status respectively
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



#performs update operation where a specific id for task is to be added and the respective task can be updated
@api_view(['GET', 'POST'])
def Taskupdate(request, pk):
    try:
        task = Task.objects.get(id=pk)
        serializer = TaskSerializer(instance=task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)   #specific handling for Task.DoesNotExist exceptions when retrieving a task by ID to return a 404 status code when the task is not found.
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


#this function is used to delete the  added task with their specific id  also cheak for exceptions and error and render out the specific http status respectively
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])   #this decorator is used to secure the delete endpoint with jwt authentication
def taskdelete(request, pk):
    try:
        task = Task.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Task.DoesNotExist:
        return Response({'error': 'Task not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)