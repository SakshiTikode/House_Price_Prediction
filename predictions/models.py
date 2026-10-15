
from django.db import models


class PredictionHistory(models.Model):
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    age = models.FloatField()
    predicted_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prediction - ₹{self.predicted_price} Lakh"
