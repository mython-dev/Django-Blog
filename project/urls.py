from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.projects, name='projects'),
    path('<int:project_id>/', views.detail_project, name='detail_project'),
    path('search/', views.Search.as_view(), name='search'),
]

