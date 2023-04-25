from rest_framework import serializers

from restful_genericapiview import models


class PublishModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pubilsh
        fields = "__all__"
