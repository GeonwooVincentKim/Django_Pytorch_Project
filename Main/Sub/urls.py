from django.conf.urls import url, include

from .views import *
from django.contrib import admin
from django.urls import path, include
from django.views import *
from . import views
from django.views.generic.base import TemplateView
from django.contrib.auth.views import (
    LoginView, LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)


# app_name = 'myapp'
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    # path('', test),
    # url(r'^post/', include('django.contrib.auth.urls')),
    path('post/', include('django.contrib.auth.urls')),

    path('post/sign/', sign, name='sign'),
    path('post/sign/signup', views.Signup.as_view(), name='signup'),
    path('post/sign/signin', LoginView.as_view(template_name='signup/signin.html'), name='signin'),
    path('post/sign/signout', LogoutView.as_view(template_name='signup/signout.html'), name='signout'),

    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='Contents/post_detail'),
    path('post/<pk>/', views.post_detail, name='post_detail'),
    path('categories/', category_list, name='category_list'),
    # path('categories/<pk>', category_detail),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('post/<pk>', post_detail),
]
