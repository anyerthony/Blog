from django.urls import path
from .views import blogViews

app_name = 'blog'

urlpatterns = [
    path('',blogViews.as_view(), name='homeView')
]