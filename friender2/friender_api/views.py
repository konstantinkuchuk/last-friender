from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from arrangement.models import User_establishment
from .serializers import EstablishmentsSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


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
    # authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = User_establishment.objects.all()
    serializer_class = EstablishmentsSerializer

class EstablishmentsListAPIViewDetail(generics.RetrieveDestroyAPIView):
    queryset = User_establishment.objects.all()
    serializer_class = EstablishmentsSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token,
            'user_id': user.pk,
            'email': user.email
        })