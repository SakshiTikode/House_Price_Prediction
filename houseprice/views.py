
from django.shortcuts import render
from pathlib import Path
import joblib

from predictions.models import PredictionHistory

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "house_price_model.pkl"

model = joblib.load(MODEL_PATH)


def home(request):
    prediction = None
    error = None

    if request.method == "POST":
        try:
            area = float(request.POST.get("area"))
            bedrooms = int(request.POST.get("bedrooms"))
            bathrooms = int(request.POST.get("bathrooms"))
            age = float(request.POST.get("age"))

            if area <= 0 or bedrooms < 1 or bathrooms < 1 or age < 0:
                raise ValueError

            features = [[area, bedrooms, bathrooms, age]]
            result = float(model.predict(features)[0])
            prediction = round(result, 2)

            # Save prediction in database
            PredictionHistory.objects.create(
                area=area,
                bedrooms=bedrooms,
                bathrooms=bathrooms,
                age=age,
                predicted_price=prediction
            )

        except Exception as e:
          print("PREDICTION ERROR:", repr(e))
          raise

    return render(
        request,
        "home.html",
        {"prediction": prediction, "error": error}
    )
