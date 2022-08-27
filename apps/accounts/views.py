from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from email import message

from apps.accounts.models import User
from apps.profiles.forms import AdminSigupForm, EmployeeSignupForm, ManagerSignupForm, AccountantSignupForm, SalesmanSignupForm, CustomerSignupForm
from django.views.generic import CreateView
from django.contrib.auth import login
from django import template
from django.contrib.auth.models import Group

from django.core.mail import send_mail, send_mass_mail
from django.core.mail import EmailMessage
from django.contrib import messages
from django.contrib.auth.decorators import login_required,user_passes_test
from datetime import datetime,timedelta,date
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse

from apps.profiles.models import Accountant, Customer, Employee, Manager, Salesman


def HomePage(request):
    return render(request, 'accounts/index.html')


class AdminSignupView(CreateView):
    model = User
    form_class = AdminSigupForm
    template_name = 'accounts/admin/admin-signup.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('Admin-Login')


# Employee Signup
class EmployeeSignupView(CreateView):
    model = User
    form_class = EmployeeSignupForm
    template_name = 'accounts/employee/emp-signup.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f'Employee Account created for {user.email}! Your Account is in Review. Once Admin approves, then you can Login')
        email_template = render_to_string('accounts/email_templates/emp_accouncreation_email.html',{'name':user.first_name,'email':user.email})
        usrEmailmsg = EmailMessage(
            'Thanks for Creating an Account',
            email_template,
            settings.EMAIL_HOST_USER,
            [user.email,'yuvra@webinoxmedia.com'],
        )
        usrEmailmsg.send(fail_silently=False)
        login(self.request, user)
        return redirect('afterlogin')


# Manager Signup
class ManagerSignupView(CreateView):
    model = User
    form_class = ManagerSignupForm
    template_name = 'accounts/manager/manager-signup.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f'Manager Account created for {user.email}! Your Account is in Review. Once Admin approves, then you can Login')
        email_template = render_to_string('accounts/email_templates/emp_accouncreation_email.html',{'name':user.first_name,'email':user.email, 'is_manager': user.is_manager})
        usrEmailmsg = EmailMessage(
            'Thanks for Creating an Account',
            email_template,
            settings.EMAIL_HOST_USER,
            [user.email,'yuvra@webinoxmedia.com'],
        )
        usrEmailmsg.send(fail_silently=False)
        login(self.request, user)
        return redirect('afterlogin')



# Accountant Signup
class AccountantSignupView(CreateView):
    model = User
    form_class = AccountantSignupForm
    template_name = 'accounts/accountant/accountant-signup.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f'Accountant Account created for {user.email}! Your Account is in Review. Once Admin approves, then you can Login')
        email_template = render_to_string('accounts/email_templates/emp_accouncreation_email.html',{'name':user.first_name,'email':user.email, 'is_accountant': user.is_accountant})
        usrEmailmsg = EmailMessage(
            'Thanks for Creating an Account',
            email_template,
            settings.EMAIL_HOST_USER,
            [user.email,'yuvra@webinoxmedia.com'],
        )
        usrEmailmsg.send(fail_silently=False)
        login(self.request, user)
        return redirect('afterlogin')



# Salesman Signup
class SalesmanSignupView(CreateView):
    model = User
    form_class = SalesmanSignupForm
    template_name = 'accounts/salesman/salesman-signup.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f'Salesman Account created for {user.email}! Your Account is in Review. Once Admin approves, then you can Login')
        email_template = render_to_string('accounts/email_templates/emp_accouncreation_email.html',{'name':user.first_name,'email':user.email, 'is_salesman': user.is_salesman})
        usrEmailmsg = EmailMessage(
            'Thanks for Creating an Account',
            email_template,
            settings.EMAIL_HOST_USER,
            [user.email,'yuvra@webinoxmedia.com'],
        )
        usrEmailmsg.send(fail_silently=False)
        login(self.request, user)
        return redirect('afterlogin')



# Customer Signup
class CustomerSignupView(CreateView):
    model = User
    form_class = CustomerSignupForm
    template_name = 'accounts/customer/customer-signup.html'

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, f'Customer Account created for {user.username}! Your Account is in Review. Once Admin approves, then you can Login')
        # email_template = render_to_string('accounts/email_templates/customer_accouncreation_email.html',{'name':user.first_name,'username':user.username})
        # usrEmailmsg = EmailMessage(
        #     'Thanks for Creating an Account',
        #     email_template,
        #     settings.EMAIL_HOST_USER,
        #     [user.email,'yuvra@webinoxmedia.com'],
        # )
        # usrEmailmsg.send(fail_silently=False)
        login(self.request, user)
        return redirect('afterlogin')





#-----------for checking user is Admin or Anything other ---------------
def is_admin(user):
    return user.groups.filter(name='ADMINs').exists()
def is_manager(user):
    return user.groups.filter(name='MANAGERs').exists()
def is_accountant(user):
    return user.groups.filter(name='ACCOUNTANTs').exists()
def is_salesman(user):
    return user.groups.filter(name='SALESMEN').exists()
def is_employee(user):
    return user.groups.filter(name='EMPLOYEEs').exists()




#---------AFTER ENTERING CREDENTIALS WE CHECK WHETHER USERNAME AND PASSWORD IS OF ADMIN,DOCTOR OR PATIENT
def afterlogin_view(request):
    # print(request.user.pkid)
    # print(request.user.id)
    # accountapproval=Manager.objects.all().filter(user_id=request.user.id, status=True).exists()
    # print(accountapproval)
    if is_admin(request.user):
        return redirect('Admin-Dahsboard')
    elif is_manager(request.user):
        # accountapproval=Manager.objects.all().filter(id=request.user.pkid,status=True)
        # accountapproval=Manager.objects.get(user__id=request.user.id)
        accountapproval=Manager.objects.all().filter(user_id=request.user.id, status=True).exists()
        if accountapproval:
            return redirect('Manager-Dahsboard')
        else:
            return render(request,'accounts/manager/manager_wait_for_approval.html')
    elif is_accountant(request.user):
        accountapproval=Accountant.objects.all().filter(user_id=request.user.id, status=True).exists()
        if accountapproval:
            return redirect('Accountant-Dahsboard')
        else:
            return render(request,'accounts/accountant/accountant_wait_for_approval.html')
    elif is_salesman(request.user):
        accountapproval=Salesman.objects.all().filter(user_id=request.user.id, status=True).exists()
        if accountapproval:
            return redirect('Salesman-Dahsboard')
        else:
            return render(request,'accounts/salesman/salesman_wait_for_approval.html')
    elif is_employee(request.user):
        accountapproval=Employee.objects.all().filter(user_id=request.user.id, status=True).exists()
        if accountapproval:
            return redirect('Employee-Dahsboard')
        else:
            return render(request,'accounts/employee/emp_wait_for_approval.html')
    else:
        # return HttpResponse("Something Went wrong. Please contact Admin. Go back to Home Page")
        return redirect("Home-Page")






#---------------------------------------------------------------------------------
#------------------------ ADMIN RELATED VIEWS START ------------------------------
#---------------------------------------------------------------------------------
@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def AdminDash(request):
    #for both table in admin dashboard
    customers=Customer.objects.all().order_by('-id')
    employee=Employee.objects.all().order_by('-id')
    manager=Manager.objects.all().order_by('-id')
    accountant=Accountant.objects.all().order_by('-id')
    salesman=Salesman.objects.all().order_by('-id')

    #for four cards
    manager_count=Manager.objects.all().filter(status=True).count()
    pending_manager_count=Manager.objects.all().filter(status=False).count()
    accountant_count=Accountant.objects.all().filter(status=True).count()
    pending_accountant_count=Accountant.objects.all().filter(status=False).count()
    salesman_count=Salesman.objects.all().filter(status=True).count()
    pending_salesman_count=Salesman.objects.all().filter(status=False).count()
    employeecount=Employee.objects.all().filter(status=True).count()
    pendingemployeecount=Employee.objects.all().filter(status=False).count()
    empcount = User.objects.all().filter(is_employee=True).count()

    context={
    'customers':customers,
    'employee': employee,
    'manager': manager,
    'accountant': accountant,
    'salesman': salesman,
    'manager_count': manager_count,
    'pending_manager_count': pending_manager_count,
    'accountant_count': accountant_count,
    'pending_accountant_count': pending_accountant_count,
    'salesman_count': salesman_count,
    'pending_salesman_count': pending_salesman_count,
    'employeecount': employeecount,
    'pendingemployeecount': pendingemployeecount,
    'empcount': empcount,
    }
    return render(request, 'accounts/admin/admin-index.html',context)






#------------------FOR APPROVING INVESTORS BY ADMIN----------------------
@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def admin_alluser_pending_view(request):
    #those whose approval are needed
    #for four cards
    manager_count=Manager.objects.all().filter(status=True).count()
    pending_manager_count=Manager.objects.all().filter(status=False).count()
    accountant_count=Accountant.objects.all().filter(status=True).count()
    pending_accountant_count=Accountant.objects.all().filter(status=False).count()
    salesman_count=Salesman.objects.all().filter(status=True).count()
    pending_salesman_count=Salesman.objects.all().filter(status=False).count()
    empcount = User.objects.all().filter(is_employee=True).count()
    employeecount=Employee.objects.all().filter(status=True).count()
    pendingemployeecount=Employee.objects.all().filter(status=False).count()
    context = {
        'empcount': empcount,
        'manager_count': manager_count,
        'pending_manager_count': pending_manager_count,
        'accountant_count': accountant_count,
        'pending_accountant_count': pending_accountant_count,
        'salesman_count': salesman_count,
        'pending_salesman_count': pending_salesman_count,
        'employeecount': employeecount,
        'pendingemployeecount': pendingemployeecount,
    }
    return render(request,'accounts/admin/admin_dashboard_cards.html',context)




@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def admin_employee_list_view(request):
    #those whose approval are needed
    #for four cards
    manager_count=Manager.objects.all().filter(status=True).count()
    pending_manager_count=Manager.objects.all().filter(status=False).count()
    managers=Manager.objects.all().filter(status=False)
    accountants=Accountant.objects.all().filter(status=False)
    pending_accountant_count=Accountant.objects.all().filter(status=False).count()
    salesmen=Salesman.objects.all().filter(status=False)
    if request.user.is_admin & request.user.is_manager & request.user.is_accountant & request.user.is_salesman:
        employees=Employee.objects.all().filter(status=False)
    else:
        employees=None
    empcount = User.objects.all().filter(is_employee=True).count()
    context = {
        'manager_count':manager_count,
        'pending_manager_count':pending_manager_count,
        'managers':managers,
        'accountants': accountants,
        'pending_accountant_count': pending_accountant_count,
        'salesmen': salesmen,
        'employees': employees,
        'empcount': empcount
    }
    return render(request,'accounts/admin/admin_approve_employees.html',context)



#---------------------------------Admin-Manager Approve-Reject End ----------------------------------------
@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def approve_manager_view(request,id):
    #approve managers
    print("clicked user id: ", id)
    manager = Manager.objects.get(id=id)
    # print(manager)
    # print(manager.id)
    # print(manager.pkid)
    # print(manager.status)
    # print(manager.user)
    # print(manager.user.id)
    # print(manager.user.pkid)
    # print(manager.user.is_active)
    manager.status=True
    manager.save()
    manager.user.save()
    email_template = render_to_string('accounts/email_templates/employee_approved_email.html',{'name':manager.user.full_name,'email':manager.user.email, 'is_manager': manager.user.is_manager})
    usrEmailmsg = EmailMessage(
        'Success - Account has been Approved',
        email_template,
        settings.EMAIL_HOST_USER,
        [manager.user.email,'yuvraj@webinoxmedia.com']
    )
    usrEmailmsg.send(fail_silently=False)
    return redirect(reverse("admin-allemp-view"))


@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def reject_manager_view(request,id):
    #reject managers
    manager = Manager.objects.get(id=id)
    manager.user.delete()
    # user.delete()
    email_template = render_to_string('accounts/email_templates/employee_reject_email.html',{'name':manager.user.full_name, 'is_manager': manager.user.is_manager})
    usrEmailmsg = EmailMessage(
        'Sorry, Account has been Rejected',
        email_template,
        settings.EMAIL_HOST_USER,
        [manager.user.email,'yuvraj@webinoxmedia.com']
    )
    usrEmailmsg.send(fail_silently=False)
    return redirect(reverse('admin-allemp-view'))

#---------------------------------Admin-Manager Approve-Reject End ------------------------------------------


#---------------------------------Admin-Accountant Approve-Reject End ----------------------------------------
@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def approve_accountant_view(request,id):
    accountant = Accountant.objects.get(id=id)
    accountant.status=True
    accountant.save()
    accountant.user.save()
    email_template = render_to_string('accounts/email_templates/employee_approved_email.html',{'name':accountant.user.full_name,'email':accountant.user.email, 'is_accountant': accountant.user.is_accountant})
    usrEmailmsg = EmailMessage(
        'Success - Account has been Approved',
        email_template,
        settings.EMAIL_HOST_USER,
        [accountant.user.email,'yuvraj@webinoxmedia.com']
    )
    usrEmailmsg.send(fail_silently=False)
    return redirect(reverse("admin-allemp-view"))


@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def reject_accountant_view(request,id):
    #reject accountants
    accountant = Accountant.objects.get(id=id)
    accountant.user.delete()
    # user.delete()
    email_template = render_to_string('accounts/email_templates/employee_reject_email.html',{'name':accountant.user.full_name, 'is_accountant': accountant.user.is_accountant})
    usrEmailmsg = EmailMessage(
        'Sorry, Account has been Rejected',
        email_template,
        settings.EMAIL_HOST_USER,
        [accountant.user.email,'yuvraj@webinoxmedia.com']
    )
    usrEmailmsg.send(fail_silently=False)
    return redirect(reverse('admin-allemp-view'))

#---------------------------------Admin-Accountant Approve-Reject End ------------------------------------------

#---------------------------------Admin-Salesman Approve-Reject End ----------------------------------------
@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def approve_salesman_view(request,id):
    #approve salesmans
    print("clicked user id: ", id)
    salesman = Salesman.objects.get(id=id)
    salesman.status=True
    salesman.save()
    salesman.user.save()
    email_template = render_to_string('accounts/email_templates/employee_approved_email.html',{'name':salesman.user.full_name,'email':salesman.user.email, 'is_salesman': salesman.user.is_salesman})
    usrEmailmsg = EmailMessage(
        'Success - Account has been Approved',
        email_template,
        settings.EMAIL_HOST_USER,
        [salesman.user.email,'yuvraj@webinoxmedia.com']
    )
    usrEmailmsg.send(fail_silently=False)
    return redirect(reverse("admin-allemp-view"))


@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def reject_salesman_view(request,id):
    #reject salesmans
    salesman = Salesman.objects.get(id=id)
    salesman.user.delete()
    # user.delete()
    email_template = render_to_string('accounts/email_templates/employee_reject_email.html',{'name':salesman.user.full_name, 'is_salesman': salesman.user.is_salesman})
    usrEmailmsg = EmailMessage(
        'Sorry, Account has been Rejected',
        email_template,
        settings.EMAIL_HOST_USER,
        [salesman.user.email,'yuvraj@webinoxmedia.com']
    )
    usrEmailmsg.send(fail_silently=False)
    return redirect(reverse('admin-allemp-view'))

#---------------------------------Admin-Salesman Approve-Reject End ------------------------------------------

#---------------------------------Admin-Employee Approve-Reject End ----------------------------------------
@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def approve_employee_view(request,id):
    #approve employees
    print("clicked user id: ", id)
    employee = Employee.objects.get(id=id)
    employee.status=True
    employee.save()
    employee.user.save()
    email_template = render_to_string('accounts/email_templates/employee_approved_email.html',{'name':employee.user.full_name,'email':employee.user.email, 'is_employee': employee.user.is_employee})
    usrEmailmsg = EmailMessage(
        'Success - Account has been Approved',
        email_template,
        settings.EMAIL_HOST_USER,
        [employee.user.email,'yuvraj@webinoxmedia.com']
    )
    usrEmailmsg.send(fail_silently=False)
    return redirect(reverse("admin-allemp-view"))


@login_required(login_url='Admin-Login')
@user_passes_test(is_admin)
def reject_employee_view(request,id):
    #reject employees
    employee = Employee.objects.get(id=id)
    employee.user.delete()
    # user.delete()
    email_template = render_to_string('accounts/email_templates/employee_reject_email.html',{'name':employee.user.full_name, 'is_employee': employee.user.is_employee})
    usrEmailmsg = EmailMessage(
        'Sorry, Account has been Rejected',
        email_template,
        settings.EMAIL_HOST_USER,
        [employee.user.email,'yuvraj@webinoxmedia.com']
    )
    usrEmailmsg.send(fail_silently=False)
    return redirect(reverse('admin-allemp-view'))

#---------------------------------Admin-Employee Approve-Reject End ------------------------------------------







# --------------------------- Manager User Views --------------------------------
#------------------------ Managers RELATED CRUD-VIEWS START ----------------
#---------------------------------------------------------------------------------
@login_required(login_url='managerlogin')
@user_passes_test(is_manager)
def ManagerDash(request):
    # print(request.user.id)
    user = User.objects.get(id=request.user.id)
    # print(user)
    accountapproval=Manager.objects.filter(user=user, status=True).exists()
    manager = Manager.objects.filter(user=user)
    if accountapproval:
        try:
            context={
                'manager':manager,
                'user':user,
                # 'accountapproval':accountapproval,
            }
            return render(request, 'accounts/manager/manager-index.html',context)
        except Exception as e:
            return HttpResponse(e)
    else:
        return redirect('afterlogin')



# --------------------------- Manager User Views End --------------------------------






# --------------------------- Accountant User Views --------------------------------
#------------------------ Accountants RELATED CRUD-VIEWS START ----------------
#---------------------------------------------------------------------------------
@login_required(login_url='accountantlogin')
@user_passes_test(is_accountant)
def AccountantDash(request):
    # print(request.user.id)
    user = User.objects.get(id=request.user.id)
    # print(user)
    accountapproval=Accountant.objects.filter(user=user, status=True).exists()
    accountant = Accountant.objects.filter(user=user)
    if accountapproval:
        try:
            context={
                'accountant':accountant,
                'user':user,
                # 'accountapproval':accountapproval,
            }
            return render(request, 'accounts/accountant/accountant-index.html',context)
        except Exception as e:
            return HttpResponse(e)
    else:
        return redirect('afterlogin')



# --------------------------- Accountant User Views End --------------------------------






# --------------------------- Salesman User Views --------------------------------
#------------------------ Salesmans RELATED CRUD-VIEWS START ----------------
#---------------------------------------------------------------------------------
@login_required(login_url='salesmanlogin')
@user_passes_test(is_salesman)
def SalesmanDash(request):
    # print(request.user.id)
    user = User.objects.get(id=request.user.id)
    # print(user)
    accountapproval=Salesman.objects.filter(user=user, status=True).exists()
    if accountapproval:
        try:
            salesman = Salesman.objects.filter(user=user)
            context={
                'salesman':salesman,
                'user':user,
                # 'accountapproval':accountapproval,
            }
            return render(request, 'accounts/salesman/salesman-index.html',context)
        except Exception as e:
            return HttpResponse(e)
    else:
        return redirect('afterlogin')



# --------------------------- Salesman User Views End --------------------------------





# --------------------------- Employee User Views --------------------------------
#------------------------ Employees RELATED CRUD-VIEWS START ----------------
#---------------------------------------------------------------------------------
@login_required(login_url='employeelogin')
@user_passes_test(is_employee)
def EmpDash(request):
    # print(request.user.id)
    user = User.objects.get(id=request.user.id)
    # print(user)
    accountapproval=Employee.objects.filter(user=user, status=True).exists()
    if accountapproval:
        try:
            employee = Employee.objects.filter(user=user)
            context={
                'employee':employee,
                'user':user,
                # 'accountapproval':accountapproval,
            }
            return render(request, 'accounts/employee/emp-index.html',context)
        except Exception as e:
            return HttpResponse(e)
    else:
        return redirect('afterlogin')


@login_required(login_url='employeelogin')
@user_passes_test(is_employee)
def employee_create_customer_view(request):
    customer_form = CustomerSignupForm()
    context = {
        'customer_form': customer_form,
    }
    return render(request, 'accounts/employee/emp-index.html', context)
# --------------------------- Employee User Views End --------------------------------