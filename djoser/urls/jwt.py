from django.conf.urls import url
from djoser.conf import settings

from rest_framework_jwt import views

from djoser import logging

if settings.ENABLE_LOGGING :
    logging.add_logging_mixin(views)

urlpatterns = [
    url(r'^jwt/create/', views.obtain_jwt_token, name='jwt-create'),
    url(r'^jwt/refresh/', views.refresh_jwt_token, name='jwt-refresh'),
    url(r'^jwt/verify/', views.verify_jwt_token, name='jwt-verify'),
]
