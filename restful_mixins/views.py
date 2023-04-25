from rest_framework import mixins
from rest_framework.generics import GenericAPIView

from restful_mixins import models
from restful_mixins.serialize.serializer import StudentModelSerializer


# Create your views here.

class StudentView(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = models.Students.objects
    serializer_class = StudentModelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class StudentDetailView(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = models.Students.objects
    serializer_class = StudentModelSerializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)

# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
#
# from restful_mixins import models
# from restful_mixins.serialize.serializer import StudentModelSerializer
#
#
# # Create your views here.
#
# class StudentView(ListCreateAPIView):
#     queryset = models.Students.objects
#     serializer_class = StudentModelSerializer
#
#
# class StudentDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = models.Students.objects
#     serializer_class = StudentModelSerializer

