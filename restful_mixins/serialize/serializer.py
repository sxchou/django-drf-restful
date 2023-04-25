from rest_framework import serializers

from restful_mixins import models


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Students
        fields = "__all__"

