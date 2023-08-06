from .views import main
from django.urls import path, include

urlpatterns = [
    path("home", main)
]
