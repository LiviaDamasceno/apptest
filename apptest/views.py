from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import BrandSerializers
from .models import Brand


class RequestTestAPI(APIView):

    def get(self, request, format=None):
        return Response ({"API": "OK"})
    
class BrandCreateViewSet(generics.CreateAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializers

class BrandRetrieveUpdateDeleteViewSet(generics.RetrieveUpdateDestroyAPIView):

    queryset = Brand.objects.all()
    serializer_class = BrandSerializers

class BrandListViewSet(generics.ListAPIView):


    queryset = Brand.objects.all()
    serializer_class = BrandSerializers


