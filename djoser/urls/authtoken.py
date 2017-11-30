from django.conf.urls import url
from djoser.conf import settings

from djoser import logging, views

if settings.ENABLE_LOGGING :
    logging.add_logging_mixin(views)

urlpatterns = [
    url(
        r'^token/create/$',
        views.TokenCreateView.as_view(),
        name='token-create'
    ),
    url(
        r'^token/destroy/$',
        views.TokenDestroyView.as_view(),
        name='token-destroy'
    ),
]
