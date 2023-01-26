from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:blog_id>/', views.detail, name='detail'),
    path('search/', views.Search.as_view(), name='search'),
]
