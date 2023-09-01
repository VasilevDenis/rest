from django.urls import path

from measurement.models import Sensor
from measurement.serializers import SensorDetailSerializer
from measurement.views import SensorList

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensor_list/', SensorList.as_view(queryset=Sensor.objects.all(), serializer_class=SensorDetailSerializer),
         name='sensor-list')
]
