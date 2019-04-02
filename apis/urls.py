from django.urls import path, include
from .views import weather

urlpatterns = [
    #path('', weather.helloworld)
    path('', weather.weather)
]