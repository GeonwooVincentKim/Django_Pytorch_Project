from .views import *
from django.contrib import admin
from django.urls import path
from django.views import *
from . import views


# app_name = 'myapp'
urlpatterns = [
    # path('', test),
    path('post/sign/', views.Signup.as_view(), name='sign'),
    # path('post/sign/signup', ),
    path('categories/', category_list, name='category_list'),
    # path('categories/<pk>', category_detail),
    path('', post_list),
    # path('post/<pk>', post_detail),
]
