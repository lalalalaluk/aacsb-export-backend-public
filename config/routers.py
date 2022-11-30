
from rest_framework.routers import DefaultRouter

from app.user.views import UserViewSet

router = DefaultRouter(trailing_slash=False)

router.register('user', UserViewSet, 'user')
