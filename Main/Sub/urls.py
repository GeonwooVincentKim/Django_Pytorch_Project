from .views import *
from django.contrib import admin
from django.urls import path
from django.views import *

urlpatterns = [
    # path('', test),
    path('categories/', category_list),
    path('categories/<pk>', category_detail),
    path('', post_list),
    path('post/<pk>', post_detail),
]
