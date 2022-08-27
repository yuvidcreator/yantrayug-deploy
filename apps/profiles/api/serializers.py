from rest_framework import serializers
from apps.profiles.models import Employee, Customer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        exclude = ["pkid", "id", "created_at", "updated_at", "user"]
        depth = 1


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        exclude = ["pkid", "id", "created_at", "updated_at", "user"]
        depth = 1