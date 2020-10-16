from django.urls import path
from .views import info_add_view

urlpatterns = [
    path('', info_add_view, name = 'info-add-view'),
]