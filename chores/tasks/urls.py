from django.urls import path
from . import views

app_name = 'tasks' 

urlpatterns = [
    path('', views.TaskListView.as_view(), name='task_list'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('create/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name="task_delete"),

    path('', views.TaskCategoryListView.as_view(), name='task_category_list'),
    path('<int:pk>/', views.TaskCategoryDetailView.as_view(), name='task_category_detail'),
    path('create/', views.TaskCreateView.as_view(), name='task_category_create'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_category_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name="task_category_delete"),
]