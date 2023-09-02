from django.urls import path

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer
from measurement.views import Sensors, Measurements

urlpatterns = [
    # Получение датчиков
    # Создание датчика
    path('sensors/', Sensors.as_view(queryset=Sensor.objects.all(),
                                     serializer_class=SensorSerializer), name='sensors'),
    # обновление датчика

    # добавление измерения
    path('measurements/', Measurements.as_view(queryset=Measurement.objects.all(),
                                               serializer_class=MeasurementSerializer), name='sensors'),

    # получение информации по датчику
    #path('sensors/<id>', Sensors.as_view(queryset=Sensor.objects.get(pk=id),
    #                                     serializer_class=SensorDetailSerializer), name='sensor')

]
