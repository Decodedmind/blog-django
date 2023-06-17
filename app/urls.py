from django.urls import path
from django.contrib import admin
from .views import (
    HomeView,
    ArticleDetailView,
    AddPostView,
    UpdatePostView,
    DeletePostView,
    AddCategoryView,
    CategoryViews,
)

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", HomeView.as_view(), name="home"),
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("add_post/", AddPostView.as_view(), name="add_post"),
    path("article/edit/<int:pk>/", UpdatePostView.as_view(), name="update_post"),
    path("article/<int:pk>/remove/", DeletePostView.as_view(), name="delete_post"),
    path("add_category/", AddCategoryView.as_view(), name="add_category"),
    path("category/<str:name>/", CategoryViews, name="category"),
]