
from django.urls import path
from . import views

urlpatterns = [
    path("", views.prediction_history, name="prediction_history"),
]
