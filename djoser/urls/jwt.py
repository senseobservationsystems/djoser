from django.conf.urls import url

from rest_framework_jwt import views

from djoser.conf import settings
from djoser import logging

if settings.ENABLE_LOGGING :
    logging.mixin(views.JSONWebTokenAPIView)

urlpatterns = [
    url(r'^jwt/create/', views.obtain_jwt_token, name='jwt-create'),
    url(r'^jwt/refresh/', views.refresh_jwt_token, name='jwt-refresh'),
    url(r'^jwt/verify/', views.verify_jwt_token, name='jwt-verify'),
]
