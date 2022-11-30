from django.shortcuts import render
from rest_framework import viewsets
from app.user.models import User
from app.user.serializers import UserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt import authentication
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.settings import api_settings
from django.conf import settings

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [IsAdminUser]

    @action(detail=False, methods=['get'])
    def test(self, request):
        print('testt' , flush=True)
        print(api_settings.DEFAULT_AUTHENTICATION_CLASSES , flush=True)
        print(api_settings.DEFAULT_PARSER_CLASSES, flush=True)
        print('qqq', flush=True)
        print(settings.REST_FRAMEWORK , flush=True)
        return Response({'status': 'password set'})
