from django.urls import path
from . import views

"""Afegim el patró URL
"""

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
