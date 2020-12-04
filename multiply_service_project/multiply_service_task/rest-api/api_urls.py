from django.urls import path

from .api_views import TApiView

urlpatterns = [
    path('multiply/<int:pk>', TApiView.as_view(), name='multiply')
]
