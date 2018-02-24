from rest_framework import serializers
from .models import Subcriber

class HelloWorldSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=6)
    age = serializers.IntegerField(required=False, min_value=10, default=10)


class SubscriberSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    email = serializers.EmailField()


class Subscriber2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Subcriber
        fields = "__all__"
