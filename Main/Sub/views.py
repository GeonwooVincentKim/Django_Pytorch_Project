from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .models import *
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404


# Create your views here.
# def test(request):
#     return HttpResponse("hello World")


def category_list(request):
    # This will get all categories,
    # you can do some filtering if you need
    # (e.g. excluding categories without posts in it)
    categories = PostCategory.objects.all()
    return render(request, "Contents/category_list.html", {"categories": categories})
    # return render(request, "index.html", {"categories": categories})


def category_detail(request, pk):
    category = get_object_or_404(PostCategory, pk=pk)
    return render(request, "Contents/category_detail.html", {"posts": category})
    # return render(request, "index.html", {"PostCategory": category})


def post_list(request):
    qs = Post.objects.all()
    posts = qs.filter(Published_at__lte=timezone.now()).order_by('published_at')
    qs = posts.order_by('Published_at')
    return render(request, "Contents/post_list.html", {"posts": qs})
    # return render(request, "index.html", {"Posts": posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # return render(request, "Contents/post_detail.html", {"post": post})
    return render(request, "index.html", {"Post": post})


class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('sign')
    template_name = 'signup/signup.html'
