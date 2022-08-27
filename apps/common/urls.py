from django.urls import path
from apps.common.views import HomePage


urlpatterns = [
    path('', HomePage, name="home-page"),
]