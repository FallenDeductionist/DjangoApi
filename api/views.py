from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Solicitud
from .serializers import SolicitudSerializer

# Create your views here.

# Lists all stocks or create a new one
# stocks/


class SolicitudList(APIView):

    def get(self, request):
        solicitudes = Solicitud.objects.all()
        serializer = SolicitudSerializer(solicitudes, many=True)
        return Response(serializer.data)

    def post(self):
        pass
