from django.urls import path
from .views import TaskListAPIView, CreateUserAPIView, CustomTokenObtainPairView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('users/', CreateUserAPIView.as_view(), name='create-user'),
]