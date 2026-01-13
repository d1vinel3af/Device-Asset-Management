from django.urls import path
from .views import test

urlpatterns = [
    path("dashboard/", test, name="test"),
]