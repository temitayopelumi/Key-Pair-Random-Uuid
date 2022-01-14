from uuid import UUID
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RandomUUIDSerializers
from .models import RandomUUID
# Create your views here.


class GetUUID(APIView):
    def  get(self, request, format=None):
        new_uuid = RandomUUID.objects.create()
        new_uuid.save()
        uuids = RandomUUID.objects.all()
        serializer = RandomUUIDSerializers(uuids, many=True)
        new_data = {}
        data = serializer.data
        for i  in range(len(data)):
            new_data[data[i]["key"]] = data[i]["value"]
        return Response(new_data, status=status.HTTP_200_OK)
