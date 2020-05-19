from .views import *
from django.contrib import admin
from django.urls import path, include
from django.views import *
from . import views


# app_name = 'myapp'
urlpatterns = [
    # path('', test),
    path('post/', include('django.contrib.auth.urls')),

    path('post/sign/', sign, name='sign'),
    path('post/sign/signup', views.Signup.as_view(), name='signup'),
    path('post/sign/signin', signin, name='signin'),
    path('categories/', category_list, name='category_list'),
    # path('categories/<pk>', category_detail),
    path('', post_list),
    # path('post/<pk>', post_detail),
]
