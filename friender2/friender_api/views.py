from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from arrangement.models import User_establishment
from .serializers import EstablishmentsSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics


# Create your views here.
# class EstablishmentsAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return User_establishment.objects.get(pk=pk)
#         except User_establishment.DoesNotExist:
#             raise Http404
#
#     def get(self, request, format=None):
#         place = User_establishment.objects.all()
#         serializer_data = EstablishmentsSerializer(place, many=True).data
#         return Response(serializer_data)
#
#     def post(self, request, format=None):
#         serializer = EstablishmentsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def put(self, request, pk, format=None):
#         place = self.get_object(pk)
#         serializer = EstablishmentsSerializer(place, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EstablishmentsListAPIView(generics.ListAPIView):
    queryset = User_establishment.objects.all()
    serializer_class = EstablishmentsSerializer

class EstablishmentsListAPIViewDetail(generics.RetrieveDestroyAPIView):
    queryset = User_establishment.objects.all()
    serializer_class = EstablishmentsSerializer