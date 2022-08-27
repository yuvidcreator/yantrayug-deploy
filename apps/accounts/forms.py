from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = [
            "email", 
            "mobile", 
            "username",
            "first_name", 
            "last_name",
            "is_employee",
            "is_admin",
            "is_manager",
            "is_accountant",
            "is_salesman",
            "is_deliveryboy",
            "is_customer",
        ]
        error_class = "error"


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            "email", 
            "mobile", 
            "first_name", 
            "last_name",
            "is_employee",
            "is_admin",
            "is_manager",
            "is_accountant",
            "is_salesman",
            "is_deliveryboy",
            "is_customer",
        ]
        error_class = "error"