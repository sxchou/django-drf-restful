from rest_framework.viewsets import ModelViewSet
from restful_modelviewset import models
from restful_modelviewset.serialize import serializer


class BookView(ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializer.BookSerializer
