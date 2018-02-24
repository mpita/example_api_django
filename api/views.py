from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from .serializers import HelloWorldSerializer, SubscriberSerializer, Subscriber2Serializer
from .models import Subcriber
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")

    user = authenticate(username=username, password=password)
    if not user:
        return Response({"error": "Login Failed"}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({"token": token.key})


class HelloWorldView(APIView):
    def get(self, request):
        return Response({"message": "Hello world!"})

    def post(self, request):
        serializer = HelloWorldSerializer(data=request.data)
        if serializer.is_valid():
            valid_data = serializer.data

            name = valid_data.get('name')
            age = valid_data.get('age')

            return Response({"message": "Hello, {}, you're {} years old".format(name, age)})
        else:
            return Response({"error": serializer.errors})


class SubscriberView(APIView):
    def get(self, request):
        subscriber_all = Subcriber.objects.all()
        serialized_subscriber = SubscriberSerializer(subscriber_all, many=True)
        return Response(serialized_subscriber.data)

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)

        if serializer.is_valid():
            subscriber_instance = Subcriber.objects.create(**serializer.data)
            return Response({"message": "Create subscriber {}".format(subscriber_instance.id)})
        else:
            return Response({"errors": serializer.errors})


class Subscriber2View(ListCreateAPIView):
    serializer_class = Subscriber2Serializer
    queryset = Subcriber.objects.all()


class SubscriberViewSet(ModelViewSet):
    serializer_class = Subscriber2Serializer
    queryset = Subcriber.objects.all()
    permission_classes = (IsAuthenticated,)
