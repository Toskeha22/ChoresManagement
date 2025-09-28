from django.urls import path
from . import views

urlpatterns = [
    path('task', views.TaskListView.as_view(), name='task_list'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_update'),
    path('taks/<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]