from rest_framework import serializers

from restful_apiview import models


class UserInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserInfo
        fields = "__all__"


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=16)
    age = serializers.IntegerField()

    def create(self, validated_data):
        instance = models.Author.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        models.Author.objects.filter(pk=instance.pk).update(**validated_data)
        return validated_data

