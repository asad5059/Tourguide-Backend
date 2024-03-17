from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .custom_permission import IsPermittedForAction
from django.contrib.auth.views import LogoutView
from .serializers import *
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import OrderingFilter

# Create your views here.

class PlaceModelViewSet(viewsets.ModelViewSet):
    queryset = PlaceInfoModel.objects.all()
    serializer_class = PlaceInfoSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsPermittedForAction,IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    filter_backends = [OrderingFilter]
    ordering_fields = ['id','name', 'rating', 'address']
    
    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)
    
    def perform_update(self, serializer):
        return serializer.save()

    
    
    
# Django 5 doesn't support logout GET view from now on. So added this.
class PatchLogoutView(LogoutView):
    http_method_names = ["get", "post", "options"]

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)