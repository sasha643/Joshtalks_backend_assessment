from django.urls import path
from .views import *

urlpatterns = [
    path('users/register', UserRegisterAPIView.as_view(), name='user-register'),
    path('tasks/create', TaskCreateAPIView.as_view(), name='create-task'),
    path('tasks/assign', TaskAssignAPIView.as_view(), name='assign-task'),
    path('tasks/users/<int:user_id>', UserTasksAPIView.as_view(), name='user-tasks'),
]