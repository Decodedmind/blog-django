from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("app.urls")),
    path("members/", include("django.contrib.auth.urls")),
    path("members/", include("members.urls")),
]
