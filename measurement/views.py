# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from measurement.serializers import MeasurementSerializer, SensorSerializer
from measurement.models import Sensor, Measurement


@api_view(['GET'])
def api(request):
    sensors = Sensor.objects.all()
    data = SensorSerializer(sensors, many=True)
    return Response(data)
