from django.urls import path
from . import views

urlpatterns = [
    path('families/', views.FamilyListView.as_view(), name='family_list'),
    path('families/create/', views.FamilyCreateView.as_view(), name='family_create'),
    path('families/<int:pk>/', views.FamilyDetailView.as_view(), name='family_detail'),
    path('families/<int:pk>/edit/', views.FamilyUpdateView.as_view(), name='family_update'),
    path('families/<int:pk>/delete/', views.FamilyDeleteView.as_view(), name='family_delete'),

    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
]