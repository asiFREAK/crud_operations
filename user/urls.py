from django.contrib import admin
from django.urls import path
from user import views as main_views

urlpatterns = [
    path('', main_views.main_html),
    path('item/', main_views.view_html)
]
