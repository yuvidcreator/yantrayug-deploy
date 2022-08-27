from django.urls import path
from apps.accounts.api.views import UserRegisterView, UserRetrieveView


urlpatterns = [
    path('signup/', UserRegisterView.as_view()),
    path('me/', UserRetrieveView.as_view()),
]