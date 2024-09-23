from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskDelete
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/delete/', TaskDelete.as_view(), name='task-delete'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),
    path('tasks/create/', TaskCreate.as_view(), name='task-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]   

