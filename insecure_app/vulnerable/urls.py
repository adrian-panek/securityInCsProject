from django.urls import path
from . import views

urlpatterns = [
    path('user_info/', views.user_info, name="user_info"),
    path("update_password/", views.update_password, name="update_password")
]