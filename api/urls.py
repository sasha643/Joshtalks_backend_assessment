from django.urls import path
from .views import TaskCreateAPIView, TaskAssignAPIView, UserTasksAPIView

urlpatterns = [
    path('create', TaskCreateAPIView.as_view(), name='create-task'),
    path('assign', TaskAssignAPIView.as_view(), name='assign-task'),
    path('users/<int:user_id>', UserTasksAPIView.as_view(), name='user-tasks'),
]