from .views import *
from django.contrib import admin
from django.urls import path
from django.views import *


# app_name = 'myapp'
urlpatterns = [
    # path('', test),
    path('sign/', Signup.as_view(), name='sign'),
    path('categories/', category_list, name='category_list'),
    # path('categories/<pk>', category_detail),
    path('', post_list),
    # path('post/<pk>', post_detail),
]
