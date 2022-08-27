from django.conf import settings
from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

from rest_framework import serializers as ser
from apps.accounts.models import *
from apps.profiles.models import Employee, Customer
from apps.accounts.api.serializers import UserSerializer
from apps.profiles.api.serializers import CustomerSerializer, EmployeeSerializer

from services import email, otp

# Create your views here.



class UserRegisterView(APIView):
    permission_classes = (permissions.AllowAny, )
    
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            print(data)

            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            mobile = data['mobile']
            password = data['password']
            re_password = data['re_password']
            is_admin = data['is_admin']
            is_manager = data['is_manager']
            is_accountant = data['is_accountant']
            is_salesman = data['is_salesman']
            is_employee = data['is_employee']
            is_customer = data['is_customer']
            if password == re_password:
                if len(password) >= 8:
                    if User.objects.filter(email=email.lower()).exists():
                        return Response("email already exists", status=status.HTTP_403_FORBIDDEN)
                    elif User.objects.filter(mobile=mobile).exists():
                        return Response("mobile already exists", status=status.HTTP_403_FORBIDDEN)
                    else:
                        if is_admin == True:
                            auser = User.objects.create_user(
                                first_name=first_name, last_name=last_name, email=email, mobile=mobile, password=password, full_name=first_name+' '+last_name, is_admin=True, is_employee=True, is_active=True
                            )
                            auser.save()
                            my_admin_group = Group.objects.get_or_create(name='ADMIN')
                            my_admin_group[0].user_set.add(auser)
                            # email_template = render_to_string(
                            #     'email_templates/admin_creation_email.html',
                            #     {'first_name':first_name, 'last_name':last_name, 'email':email}
                            # )
                            # adminEmailmsg = EmailMessage(
                            #     'Thanks for Creating an Account',
                            #     email_template,
                            #     settings.EMAIL_HOST_USER,
                            #     [user.email],
                            # )
                            # adminEmailmsg.send(fail_silently=False)
                            return Response(
                                {'sucess': 'Admin Account Created Successfully'},
                                status=status.HTTP_201_CREATED
                            )

                        elif is_employee == True:
                            user = User.objects.create_user(
                                first_name=first_name, last_name=last_name, email=email, mobile=mobile, password=password, full_name=first_name+' '+last_name, is_employee=True, is_active=True
                            )
                            user.save()
                            employee = Employee.objects.create(user=user)
                            employee.save()
                            my_employees_group = Group.objects.get_or_create(name='EMPLOYEES')
                            my_employees_group[0].user_set.add(user)
                            # email_template = render_to_string(
                            #     'email_templates/employer_creation_email.html',
                            #     {'first_name':first_name, 'last_name':last_name, 'email':email}
                            # )
                            # adminEmailmsg = EmailMessage(
                            #     'Thanks for Creating an Account',
                            #     email_template,
                            #     settings.EMAIL_HOST_USER,
                            #     [user.email],
                            # )
                            # adminEmailmsg.send(fail_silently=False)
                            return Response(
                                {'sucess': 'Employee Account Created Successfully'},
                                status=status.HTTP_201_CREATED
                            )

                        elif is_manager == True:
                            user = User.objects.create_user(
                                first_name=first_name, last_name=last_name, email=email, mobile=mobile, password=password, full_name=first_name+' '+last_name, is_employee=True, is_active=True
                            )
                            user.save()
                            manager = Employee.objects.create(user=user, is_manager=True)
                            manager.save()
                            my_managers_group = Group.objects.get_or_create(name='MANAGERS')
                            my_managers_group[0].user_set.add(user)
                            # email_template = render_to_string(
                            #     'email_templates/employer_creation_email.html',
                            #     {'first_name':first_name, 'last_name':last_name, 'email':email}
                            # )
                            # adminEmailmsg = EmailMessage(
                            #     'Thanks for Creating an Account',
                            #     email_template,
                            #     settings.EMAIL_HOST_USER,
                            #     [user.email],
                            # )
                            # adminEmailmsg.send(fail_silently=False)
                            return Response(
                                {'sucess': 'Manager Account Created Successfully'},
                                status=status.HTTP_201_CREATED
                            )

                        elif is_accountant == True:
                            user = User.objects.create_user(
                                first_name=first_name, last_name=last_name, email=email, mobile=mobile, password=password, full_name=first_name+' '+last_name, is_employee=True, is_active=True
                            )
                            user.save()
                            accountant = Employee.objects.create(user=user, is_accountant=True)
                            accountant.save()
                            my_accountants_group = Group.objects.get_or_create(name='ACCOUNTANT')
                            my_accountants_group[0].user_set.add(user)
                            # email_template = render_to_string(
                            #     'email_templates/employer_creation_email.html',
                            #     {'first_name':first_name, 'last_name':last_name, 'email':email}
                            # )
                            # adminEmailmsg = EmailMessage(
                            #     'Thanks for Creating an Account',
                            #     email_template,
                            #     settings.EMAIL_HOST_USER,
                            #     [user.email],
                            # )
                            # adminEmailmsg.send(fail_silently=False)
                            return Response(
                                {'sucess': 'Accountants Account Created Successfully'},
                                status=status.HTTP_201_CREATED
                            )

                        elif is_salesman == True:
                            user = User.objects.create_user(
                                first_name=first_name, last_name=last_name, email=email, mobile=mobile, password=password, full_name=first_name+' '+last_name, is_employee=True, is_active=True
                            )
                            user.save()
                            salesman = Employee.objects.create(user=user, is_salesman=True, is_deliveryboy=True)
                            salesman.save()
                            my_salesmens_group = Group.objects.get_or_create(name='SALESMEN')
                            my_salesmens_group[0].user_set.add(user)
                            # email_template = render_to_string(
                            #     'email_templates/employer_creation_email.html',
                            #     {'first_name':first_name, 'last_name':last_name, 'email':email}
                            # )
                            # adminEmailmsg = EmailMessage(
                            #     'Thanks for Creating an Account',
                            #     email_template,
                            #     settings.EMAIL_HOST_USER,
                            #     [user.email],
                            # )
                            # adminEmailmsg.send(fail_silently=False)
                            return Response(
                                {'sucess': 'Salesman Account Created Successfully'},
                                status=status.HTTP_201_CREATED
                            )

                        else:
                            user = User.objects.create_user(
                                first_name=first_name, last_name=last_name, email=email, mobile=mobile, password=password, full_name=first_name+' '+last_name, is_customer=True, is_active=True
                            )
                            user.save()
                            customer = Customer.objects.create(user=user)
                            customer.save()
                            my_customers_group = Group.objects.get_or_create(name='CUSTOMERS')
                            my_customers_group[0].user_set.add(user)
                            # email_template = render_to_string(
                            #     'email_templates/customer_creation_email.html',
                            #     {'first_name':first_name, 'last_name':last_name, 'email':email}
                            # )
                            # adminEmailmsg = EmailMessage(
                            #     'Thanks for Creating an Account',
                            #     email_template,
                            #     settings.EMAIL_HOST_USER,
                            #     [user.email],
                            # )
                            # adminEmailmsg.send(fail_silently=False)
                            return Response(
                                {'sucess': 'Customer Account Created Successfully'},
                                status=status.HTTP_201_CREATED
                            )
                else:
                    return Response(
                        {'error': 'Password must be 8 charachters in length'},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'error': 'Password Do not match'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except:
            return Response(
                {'error': 'Something went wrong while Creating an Account.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )




class UserRetrieveView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            print(user.pkid)
            print(user.is_employee)
            if user.is_admin:
                u_sr = UserSerializer(user)
                # emp_sr = EmployeeSerializer(Employee.objects.filter(email=user).first())
                serializer = [u_sr.data]
                return Response(
                    serializer,
                    status=status.HTTP_200_OK
                )
            elif user.is_employee:
                u_sr = UserSerializer(user)
                emp_sr = EmployeeSerializer(Employee.objects.filter(user=user).first())
                serializer = [u_sr.data, emp_sr.data]
                return Response(
                    serializer,
                    status=status.HTTP_200_OK
                )
            elif user.is_customer:
                u_sr = UserSerializer(user)
                cust_sr = CustomerSerializer(Customer.objects.filter(user=user).first())
                serializer = [u_sr.data, cust_sr.data]
                return Response(
                    serializer,
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"error": "Something wrong in Serializer"}
                )
        except:
            return Response(
                {'error': 'Something went wrong when retrieving user'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )