from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskCreate(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        print("Current user:", user)  # Для отладки
        if user.is_authenticated:
            serializer.save(user=user)
        else:
            print("User is not authenticated!")
            raise ValueError("User must be authenticated.")

class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

