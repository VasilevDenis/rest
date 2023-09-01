from django.urls import path
from measurement.views import api

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('', api),
]
