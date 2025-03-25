from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Task, User
from .serializers import *
from http import HTTPStatus


class TaskCreateAPIView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "reason": HTTPStatus.BAD_REQUEST.phrase,
                    "message": serializer.errors
                },
                status=HTTPStatus.BAD_REQUEST.value
            )

        self.perform_create(serializer)
        return Response(
            {
                "reason": HTTPStatus.CREATED.phrase,
                "message": "Task created successfully"
            },
            status=HTTPStatus.CREATED.value
        )

    def perform_create(self, serializer):
        serializer.save()


class TaskAssignAPIView(APIView):
    def post(self, request):
        serializer = TaskAssignSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {
                    "reason": HTTPStatus.BAD_REQUEST.phrase,
                    "message": serializer.errors
                },
                status=HTTPStatus.BAD_REQUEST.value
            )

        task_id = serializer.validated_data.get('task_id')
        user_ids = serializer.validated_data.get('user_ids')

        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response(
                {
                    "reason": HTTPStatus.NOT_FOUND.phrase,
                    "message": "Task does not exist"
                },
                status=HTTPStatus.NOT_FOUND.value
            )

        users = User.objects.filter(id__in=user_ids)
        if not users.exists():
            return Response(
                {
                    "reason": HTTPStatus.NOT_FOUND.phrase,
                    "message": "No valid users found to assign"
                },
                status=HTTPStatus.NOT_FOUND.value
            )

        task.assigned_users.set(users)
        task.save()

        return Response(
            {
                "reason": HTTPStatus.OK.phrase,
                "message": "Task assigned successfully"
            },
            status=HTTPStatus.OK.value
        )


class UserTasksAPIView(APIView):
    def get(self, request, user_id: int):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response(
                {
                    "reason": HTTPStatus.NOT_FOUND.phrase,
                    "message": "User does not exist"
                },
                status=HTTPStatus.NOT_FOUND.value
            )

        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(
            {
                "reason": HTTPStatus.OK.phrase,
                "message": "Tasks fetched successfully",
                "data": serializer.data
            },
            status=HTTPStatus.OK.value
        )
