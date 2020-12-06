from django.urls import path

from .api_views import TApiView

urlpatterns = [
    path('json/', TApiView.as_view(), name='multiply')
]
