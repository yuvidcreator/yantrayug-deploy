from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.utils.safestring import mark_safe

from apps.accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from apps.accounts.models import User
from apps.accounts.views import is_admin


class UserAdmin(BaseUserAdmin):
    ordering = ["email"]
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = [
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "mobile",
        # "is_employee",
        # "is_customer",
        "user_rol",
        # "is_staff",
        "is_active",
    ]
    list_display_links = list_display
    list_filter = [
        "email",
        "mobile",
        "first_name",
        "last_name",
        "is_customer",
        "is_active",
    ]

    def user_rol(self, obj):
        if obj.is_superuser:
            return f"Super Admin"
        elif obj.is_admin:
            return f"Admin"
        elif obj.is_manager:
            return f"Manager"
        elif obj.is_accountant:
            return f"Accountant"
        elif obj.is_salesman or obj.is_deliveryboy:
            return f"Salesman"
        elif obj.is_customer:
            return f"Customer"
        else:
            return f"Employee"

    fieldsets = (
        (
            _("Login Credentials"),
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Personal Information"),
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "full_name",
                    "mobile",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_superuser",
                    "is_active",
                    "is_staff",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            _("Employee Positions"),
            {
                "fields": (
                    "is_admin",
                    "is_employee",
                    "is_manager",
                    "is_accountant",
                    "is_salesman",
                    "is_deliveryboy",
                    "is_customer"
                )
            }
        ),
        (_("Important Dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            "User Information", 
            {
                "fields": (
                    "username", 
                    "email", 
                    "password1", 
                    "password2", 
                    "is_staff", 
                    "is_active", 
                    "is_employee",
                    "is_manager",
                    "is_accountant",
                    "is_salesman",
                    "is_deliveryboy",
                    "is_customer"
                ),
            },
        ),
        (
            "Groups And Permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
    )
    search_fields = ["username", "email", "mobile", "first_name", "last_name"]


admin.site.register(User, UserAdmin)