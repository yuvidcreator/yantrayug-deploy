from dataclasses import fields
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from django.contrib.auth.models import Group

from apps.accounts.models import User
from apps.profiles.models import Employee, Manager, Accountant, Salesman, Customer


#for admin signup
class AdminSigupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email','mobile','password1','password2']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.full_name = f"{user.first_name} {user.last_name}"
        user.is_admin = True
        user.is_employee = True
        user.is_active = True
        user.save()
        emp = Employee.objects.create(user=user)
        emp.save()
        my_admin_group = Group.objects.get_or_create(name='ADMINs')
        my_admin_group[0].user_set.add(user)
        my_employees_group = Group.objects.get_or_create(name='EMPLOYEEs')
        my_employees_group[0].user_set.add(user)
        return user



#for Employee signup
class EmployeeSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile',  'password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.mobile = self.cleaned_data.get('mobile')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.full_name = f"{user.first_name} {user.last_name}"
        user.is_active = True
        user.save()
        emp = Employee.objects.create(user=user)
        emp.save()
        my_employees_group = Group.objects.get_or_create(name='EMPLOYEEs')
        my_employees_group[0].user_set.add(user)
        return user



#for Manager signup
class ManagerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile',  'password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.mobile = self.cleaned_data.get('mobile')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.full_name = f"{user.first_name} {user.last_name}"
        user.is_active = True
        user.is_manager = True
        user.is_employee = True
        user.save()
        mngr = Manager.objects.create(user=user)
        mngr.save()
        my_managers_group = Group.objects.get_or_create(name='MANAGERs')
        my_managers_group[0].user_set.add(user)
        my_employees_group = Group.objects.get_or_create(name='EMPLOYEEs')
        my_employees_group[0].user_set.add(user)
        return user



#for Accountant signup
class AccountantSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile',  'password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.mobile = self.cleaned_data.get('mobile')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.full_name = f"{user.first_name} {user.last_name}"
        user.is_active = True
        user.is_employee = True
        user.is_accountant = True
        user.save()
        accontnt = Accountant.objects.create(user=user)
        accontnt.save()
        my_accountants_group = Group.objects.get_or_create(name='ACCOUNTANTs')
        my_accountants_group[0].user_set.add(user)
        my_employees_group = Group.objects.get_or_create(name='EMPLOYEEs')
        my_employees_group[0].user_set.add(user)
        return user




#for Customer signup
class SalesmanSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile',  'password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.mobile = self.cleaned_data.get('mobile')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.full_name = f"{user.first_name} {user.last_name}"
        user.is_active = True
        user.is_employee = True
        user.is_salesman = True
        user.is_deliveryboy = True
        user.save()
        salesman = Salesman.objects.create(user=user)
        salesman.save()
        my_salesmen_group = Group.objects.get_or_create(name='SALESMEN')
        my_salesmen_group[0].user_set.add(user)
        my_employees_group = Group.objects.get_or_create(name='EMPLOYEEs')
        my_employees_group[0].user_set.add(user)
        return user



#for Customer signup
class EmployeeSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile',  'password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.mobile = self.cleaned_data.get('mobile')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.full_name = f"{user.first_name} {user.last_name}"
        user.is_active = True
        user.is_employee = True
        user.save()
        emplyoee = Employee.objects.create(user=user)
        emplyoee.save()
        my_employees_group = Group.objects.get_or_create(name='EMPLOYEEs')
        my_employees_group[0].user_set.add(user)
        return user



#for Customer signup
class CustomerSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile',  'password1', 'password2']
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.mobile = self.cleaned_data.get('mobile')
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.full_name = f"{user.first_name} {user.last_name}"
        user.is_active = True
        user.is_customer = True
        user.save()
        customer = Customer.objects.create(user=user)
        customer.save()
        my_customer_group = Group.objects.get_or_create(name='CUSTOMERs')
        my_customer_group[0].user_set.add(user)
        return user





class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"




class ManagerProfileForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"



class AccountantProfileForm(forms.ModelForm):
    class Meta:
        model = Accountant
        fields = "__all__"



class SalesmanProfileForm(forms.ModelForm):
    class Meta:
        model = Salesman
        fields = "__all__"




class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Salesman
        fields = "__all__"