from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from restful_genericapiview import models
from restful_genericapiview.serialize.serializer import PublishModelSerializer


# Create your views here.
class PublishView(GenericAPIView):
    queryset = models.Pubilsh.objects
    serializer_class = PublishModelSerializer

    def get(self, request):
        ser = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(ser.data)

    def post(self, request):
        ser = self.get_serializer(data=request.data)
        if not ser.is_valid():
            return Response(ser.errors)
        ser.save()
        return Response(ser.data)


class PublishDetailView(GenericAPIView):
    queryset = models.Pubilsh.objects
    serializer_class = PublishModelSerializer

    def get(self, request, pk):
        ser = self.get_serializer(instance=self.get_object())
        return Response(ser.data)

    def put(self, request, pk):
        ser = self.get_serializer(data=request.data, instance=self.get_object())
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

    def delete(self, request, pk):
        self.get_object().delete()
        return Response()

