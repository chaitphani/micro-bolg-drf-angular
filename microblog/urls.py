from django.urls import path, include
from rest_framework import routers

from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('api/users', views.UserApiview.as_view(), name='users'),
    path('api/posts', views.BlogPostApiView.as_view(), name='posts'),

]