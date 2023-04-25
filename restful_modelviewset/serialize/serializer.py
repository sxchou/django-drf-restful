from rest_framework import serializers

from restful_modelviewset import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = "__all__"

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('输入的价格不能为负')
        return value

    def validate_name(self, value):
        if value.endswith('书'):
            return value
        raise serializers.ValidationError('书名必须以书结尾')
