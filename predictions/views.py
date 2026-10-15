
from django.shortcuts import render
from .models import PredictionHistory


def prediction_history(request):
    predictions = PredictionHistory.objects.all().order_by("-created_at")

    return render(
        request,
        "history.html",
        {"predictions": predictions}
    )
