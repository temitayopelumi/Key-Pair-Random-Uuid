import imp
from .views import GetUUID
from django.urls import path


urlpatterns = [
    path('get-uuid/', GetUUID.as_view(), name='Get UUID'),
]