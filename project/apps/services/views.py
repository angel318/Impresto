from django.shortcuts import render

from rest_framework import status
from rest_framework.views import Response, APIView
from rest_framework import permissions
from project.common.pagination import PageNumberPagination

from django.http import HttpResponse
from . import serializers
from . import models

#SERVICIOS
class ServicesView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ServicesSerializer

    def get(self, request, format=None, pk=None):
        if pk == None:
            paginator = PageNumberPagination()
            objects = models.Services.objects.filter(is_active = True).all()
            result_page = paginator.paginate_queryset(objects, request)
            serializer = serializers.ServicesSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)
        else:
            objects = models.Services.objects.filter(is_active = True).get(pk=pk)
            serializer = serializers.ServicesSerializer(objects, many=False)

            return Response (serializer.data)

    def post(self, request):
        serializer = serializers.ServicesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                owner=self.request.user,
                is_active=True
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = models.Services.objects.get(pk=pk)
        service.is_active = False
        service.save()

        return Response(None, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        service = models.Services.objects.get(pk=pk)
        serializer = serializers.ServicesSerializer(service, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#TAMAÑOS DE HOJAS
class SheetSizesView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.SheetSizesSerializer

    def get(self, request, format=None, pk=None):
        if pk == None:
            paginator = PageNumberPagination()
            objects = models.SheetSizes.objects.filter(is_active = True).all()
            result_page = paginator.paginate_queryset(objects, request)
            serializer = serializers.SheetSizesSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)
        else:
            objects = models.SheetSizes.objects.filter(is_active = True).get(pk=pk)
            serializer = serializers.SheetSizesSerializer(objects, many=False)

            return Response (serializer.data)


    def post(self, request):
        serializer = serializers.SheetSizesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                owner=self.request.user,
                is_active=True
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = models.SheetSizes.objects.get(pk=pk)
        service.is_active = False
        service.save()

        return Response(None, status=status.HTTP_200_OK)

    def patch(self,request,pk):
        sheetSize = models.SheetSizes.objects.get(pk=pk)
        serializer = serializers.SheetSizesSerializer(sheetSize, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#TIPOS DE HOJA
class SheetTypesView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.SheetTypesSerializer

    def get(self, request, format=None, pk=None):
        if pk == None:
            paginator = PageNumberPagination()
            objects = models.SheetTypes.objects.filter(is_active = True).all()
            result_page = paginator.paginate_queryset(objects, request)
            serializer = serializers.SheetTypesSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)
        else:
            objects = models.SheetTypes.objects.filter(is_active = True).get(pk=pk)
            serializer = serializers.SheetTypesSerializer(objects, many=False)

            return Response (serializer.data)

    def post(self, request):
        serializer = serializers.SheetTypesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                owner=self.request.user,
                is_active=True
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = models.SheetTypes.objects.get(pk=pk)
        service.is_active = False
        service.save()

        return Response(None, status=status.HTTP_200_OK)

    def patch(self,request,pk):
        sheetType = models.SheetTypes.objects.get(pk=pk)
        serializer = serializers.SheetTypesSerializer(sheetType, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#EXTRAS
class ExtrasView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = serializers.ExtrasSerializer

    def get(self, request, format=None, pk=None):
        if pk == None:
            paginator = PageNumberPagination()
            objects = models.Extras.objects.filter(is_active = True).all()
            result_page = paginator.paginate_queryset(objects, request)
            serializer = serializers.ExtrasSerializer(result_page, many=True)

            return paginator.get_paginated_response(serializer.data)
        else:
            objects = models.Extras.objects.filter(is_active = True).get(pk=pk)
            serializer = serializers.ExtrasSerializer(objects, many=False)

            return Response (serializer.data)


    def post(self, request):
        serializer = serializers.ExtrasSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(
                owner=self.request.user,
                is_active=True
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        service = models.Extras.objects.get(pk=pk)
        service.is_active = False
        service.save()

        return Response(None, status=status.HTTP_200_OK)

    def patch(self,request,pk):
        extra = models.Extras.objects.get(pk=pk)
        serializer = serializers.ExtrasSerializer(extra, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
