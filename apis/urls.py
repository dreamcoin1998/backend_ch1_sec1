from django.urls import path, include
from .views import weather, menu, image

urlpatterns = [
    #path('', weather.helloworld)
    #path('', weather.weather)
    path('weather', weather.weather),
    path('menu', menu.get_menu),
    # path('image', image.image),
    # path('imagetext', image.image_text),
    path('image', image.ImageView.as_view())
]