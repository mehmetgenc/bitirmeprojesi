from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from bitirme.models import Kampanya
from bitirme.serializers import KampanyaSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def kampanya_list(request):
    """
    List all snippets, or create a new snippet.
    """
    if request.method == 'GET':
        kampanyalar = Kampanya.objects.all()
        serializer = KampanyaSerializer(kampanyalar, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = KampanyaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def kampanya_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        kampanya = Kampanya.objects.get(pk=pk)
    except Kampanya.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = KampanyaSerializer(kampanya)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = KampanyaSerializer(kampanya, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kampanya.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class JSONResponse(HttpResponse):
#
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
# @csrf_exempt
# def kampanya_list(request):
#
#     if request.method == 'GET':
#         kampanyalar = Kampanya.objects.all()
#         serializer = KampanyaSerializer(kampanyalar, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = KampanyaSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def kampanya_detail(request, pk):
#
#     try:
#         kampanya = Kampanya.objects.get(pk=pk)
#     except Kampanya.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = KampanyaSerializer(kampanya)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = KampanyaSerializer(kampanya, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         kampanya.delete()
#         return HttpResponse(status=204)