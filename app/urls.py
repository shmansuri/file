from django.urls import path
from app import views

urlpatterns = [
    path('uploadfile/', views.upload_file)
]
