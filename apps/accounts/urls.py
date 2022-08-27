from django.urls import path
from apps.accounts.models import *
from apps.accounts.views import *
from apps.profiles.models import *
from apps.profiles.views import *

from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('', HomePage, name="Home-Page"),
    
    path('afterlogin/', afterlogin_view, name='afterlogin'),
    path('logout/', LogoutView.as_view(template_name='accounts/index.html'),name='logout'),

    #----------------------SIGNUP URLS------------------------------------
    path('adminsignup/', AdminSignupView.as_view()),
    path('managersignup/', ManagerSignupView.as_view(), name="Manager-Signup"),
    path('accountantsignup/', AccountantSignupView.as_view(), name="Accountant-Signup"),
    path('salesmansignup/', SalesmanSignupView.as_view(), name="Salesman-Signup"),
    path('employeesignup/', EmployeeSignupView.as_view(), name="Employee-Signup"),
    path('customersignup/', CustomerSignupView.as_view(), name="Customer-Signup"),

    #----------------------LOGIN URLS------------------------------------
    path('adminlogin/', LoginView.as_view(template_name='accounts/admin/admin-login.html'), name="Admin-Login"),
    # path('adminlogin/', AdminLoginView, name="Admin-Login"),
    # path('customerlogin/', CustomerLoginView, name="customerlogin"),

    path('customerlogin/', LoginView.as_view(template_name='accounts/customer/customer-login.html'), name="customerlogin"),
    path('managerlogin/', LoginView.as_view(template_name='accounts/manager/manager-login.html'), name="managerlogin"),
    path('accountantlogin/', LoginView.as_view(template_name='accounts/accountant/accountant-login.html'), name="accountantlogin"),
    path('salesmanlogin/', LoginView.as_view(template_name='accounts/salesman/salesman-login.html'), name="salesmanlogin"),
    path('employeelogin/', LoginView.as_view(template_name='accounts/employee/emp-login.html'), name="employeelogin"),
    

    #----------------------DASHBOARDS URLS------------------------------------
    path('admindash/', AdminDash, name="Admin-Dahsboard"),
    path('admin-allemp/', admin_alluser_pending_view, name="admin_allemp"),
    # path('adminprofile/', AdminProfile, name="Admin-Profile"),

    #----------------------ADMIN-MANAGERs CRUD-APPROVALS URLS--------------------------------
    path('admin-approve-employee/', admin_employee_list_view, name='admin-allemp-view'),
    path('approve-manager/<int:id>/', approve_manager_view, name='approve-manager'),
    path('reject-manager/<int:id>/', reject_manager_view, name='reject-manager'),

    #----------------------ADMIN-ACCOUNTANTs CRUD-APPROVALS URLS--------------------------------
    path('approve-accountant/<int:id>/', approve_accountant_view, name='approve-accountant'),
    path('reject-accountant/<int:id>/', reject_accountant_view, name='reject-accountant'),

    #----------------------ADMIN-SALESMEN CRUD-APPROVALS URLS--------------------------------
    path('approve-salesman/<int:id>/', approve_salesman_view, name='approve-salesman'),
    path('reject-salesman/<int:id>/', reject_salesman_view, name='reject-salesman'),

    #----------------------ADMIN-EMPLOYEEs CRUD-APPROVALS URLS--------------------------------
    path('approve-employee/<int:id>/', approve_employee_view, name='approve-employee'),
    path('reject-employee/<int:id>/', reject_employee_view, name='reject-employee'),

    #----------------------Manager DASHBOARDS URLS------------------------------------
    path('managerdash/', ManagerDash, name="Manager-Dahsboard"),
    # path('managerprofile/', ManagerProfile, name="Manager-Profile"),

    #----------------------Accountant DASHBOARDS URLS------------------------------------
    path('accountantdash/', AccountantDash, name="Accountant-Dahsboard"),
    # path('managerprofile/', ManagerProfile, name="Manager-Profile"),

    #----------------------Salesman DASHBOARDS URLS------------------------------------
    path('salesmandash/', SalesmanDash, name="Salesman-Dahsboard"),
    # path('managerprofile/', ManagerProfile, name="Manager-Profile"),

    #----------------------Employee DASHBOARDS URLS------------------------------------
    path('empdash/', EmpDash, name="Emp-Dahsboard"),
    path('create-customer/', employee_create_customer_view, name="emp-create-customer"),
    # path('managerprofile/', ManagerProfile, name="Manager-Profile"),
]