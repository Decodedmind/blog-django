from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ["-post_date", "-id"]


def CategoryViews(request, name):
    category_post = Post.objects.filter(
        category=name.replace(
            "-",
            " ",
        )
    )
    return render(
        request,
        "categories.html",
        {"name": name.title().replace("-", " "), "category_post": category_post},
    )


class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"
    # fields = "__all__"


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"
    success_url = reverse_lazy("home")
    # fields = ["title", "title_tag", "body"]


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy("home")
    # fields = ["title", "title_tag", "body"]


class AddCategoryView(CreateView):
    model = Category

    template_name = "add_category.html"
    fields = "__all__"
    success_url = reverse_lazy("home")
