from rest_framework.generics import ListAPIView
from rest_framework import exceptions

from app.models import User
from app.serializers import UserSerializer
from app.utils.errors import Error
from app.views import BaseWebsocket


class Test1APIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        BaseWebsocket.group_send("123wzj", "1231233123")
        return self.queryset.all()


class Test2APIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.query_params.get("flag"):
            raise exceptions.ValidationError(Error.API_ERROR)
        return self.queryset.all()