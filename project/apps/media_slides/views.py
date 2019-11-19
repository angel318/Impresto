from django.shortcuts import render

from rest_framework import status
from rest_framework.views import Response, APIView
from rest_framework import permissions
from project.common.pagination import PageNumberPagination

from django.http import HttpResponse
from . import serializers
from . import models

# Create your views here.
class SlidesView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.SlidesSerializer

    def get(self, request, format=None, pk=None):
        if pk == None:
            paginator = PageNumberPagination()
            objects = models.Slides.objects.filter(is_active = True).all()
            result_page = paginator.paginate_queryset(objects, request)
            serializer = serializers.SlidesSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)
        else:
            objects = models.Slides.objects.filter(is_active = True).get(pk=pk)
            serializer = serializers.SlidesSerializer(objects, many=False)

            return Response (serializer.data)

    def post(self, request):
        serializer = serializers.SlidesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                owner=self.request.user,
                is_active=True
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        slide = models.Slides.objects.get(pk=pk)
        slide.is_active = False
        slide.save()

        return Response(None, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        slide = models.Slides.objects.get(pk=pk)
        serializer = serializers.SlidesSerializer(slide, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
