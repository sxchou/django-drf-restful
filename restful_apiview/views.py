from rest_framework.response import Response
from rest_framework.views import APIView

from restful_apiview import models
from restful_apiview.serialize import serializer


# Create your views here.
class UserInfoView(APIView):
    def get(self, request):
        query = models.UserInfo.objects.all()
        ser = serializer.UserInfoModelSerializer(instance=query, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = serializer.UserInfoModelSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors)
        ser.save()
        return Response(ser.data)


class UserInfoDetailView(APIView):
    def get(self, request, pk):
        row_obj = models.UserInfo.objects.get(pk=pk)
        ser = serializer.UserInfoModelSerializer(instance=row_obj)
        return Response(ser.data)

    def put(self, request, pk):
        row_obj = models.UserInfo.objects.get(pk=pk)
        ser = serializer.UserInfoModelSerializer(instance=row_obj, data=request.data)
        if not ser.is_valid():
            return Response(ser.errors)
        ser.save()
        return Response(ser.data)

    def delete(self, request, pk):
        models.UserInfo.objects.get(pk=pk).delete()
        return Response()


class AuthorView(APIView):
    def get(self, request):
        query = models.Author.objects.all()
        ser = serializer.AuthorSerializer(instance=query, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = serializer.AuthorSerializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors)
        ser.save()
        return Response(ser.data)


class AuthorDetailView(APIView):
    def get(self, request, pk):
        row_obj = models.Author.objects.get(pk=pk)
        ser = serializer.AuthorSerializer(instance=row_obj)
        return Response(ser.data)

    def put(self, request, pk):
        row_obj = models.Author.objects.get(pk=pk)
        ser = serializer.AuthorSerializer(instance=row_obj, data=request.data)
        if not ser.is_valid():
            return Response(ser.errors)
        ser.save()
        return Response(ser.data)

    def delete(self, request, pk):
        models.Author.objects.get(pk=pk).delete()
        return Response()
