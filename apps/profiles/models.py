import datetime
from django.utils import timezone
import uuid
from django.utils.crypto import get_random_string
from django.conf import settings
from django.db import models
from apps.common.models import TimeStampUUIDModel
from django.utils.translation import gettext_lazy as _
from apps.accounts.models import User
# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'user_{0}/{1}'.format(instance.user.id, filename)

class Gender(models.TextChoices):
    MALE = "Male", _("Male")
    FEMALE = "Female", _("Female")
    OTHER = "Other", _("Other")


# Manager models
class Employee(TimeStampUUIDModel):
    user = models.ForeignKey(User, related_name="employees", on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, verbose_name=_("Employee ID"), blank=True, null=True)
    is_mobile_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="employees/profile_pics", blank=True, verbose_name=_("Employees Profile Image")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender = models.CharField(max_length=20, verbose_name=_("Gender"), choices=Gender.choices, default="--", blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 1"))
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 2"))
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"))
    about_me = models.TextField(blank=True, verbose_name=_("About Me"))
    salary = models.IntegerField(blank=True, null=True, verbose_name=_("Salary"))
    bank_account_details = models.TextField(blank=True, null=True, verbose_name=_("Bank Details"), )
    qualification = models.CharField(max_length=255, blank=True, verbose_name=_("Educational Qualification"))
    work_experience = models.CharField(max_length=75, blank=True, verbose_name=_("Work Experience"))
    status = models.BooleanField(default=False, verbose_name=_("Is Approved by Admin"))

    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_mobile(self):
        return self.user.mobile

    @property
    def get_user_id(self):
        return self.user.id

    @property
    def get_user_pkid(self):
        return self.user.pkid

    @property
    def get_user_role(self):
        if self.user.is_employee:
            return f"Employee"

    def __str__(self):
        return f"{self.user.email}"



# Manager models
class Manager(TimeStampUUIDModel):
    user = models.ForeignKey(User, related_name="managers", on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, verbose_name=_("Employee ID"), blank=True, null=True)
    is_mobile_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="managers/profile_pics", blank=True, verbose_name=_("Manager Profile Image")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender = models.CharField(max_length=20, verbose_name=_("Gender"), choices=Gender.choices, default="--", blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 1"))
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 2"))
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"))
    about_me = models.TextField(blank=True, verbose_name=_("About Me"))
    salary = models.IntegerField(blank=True, null=True, verbose_name=_("Salary"))
    bank_account_details = models.TextField(blank=True, null=True, verbose_name=_("Bank Details"), )
    qualification = models.CharField(max_length=255, blank=True, verbose_name=_("Educational Qualification"))
    work_experience = models.CharField(max_length=75, blank=True, verbose_name=_("Work Experience"))
    status = models.BooleanField(default=False, verbose_name=_("Is Approved by Admin"))

    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_mobile(self):
        return self.user.mobile

    @property
    def get_user_id(self):
        return self.user.id

    @property
    def get_user_pkid(self):
        return self.user.pkid

    @property
    def get_user_role(self):
        if self.user.is_manager:
            return f"Manager"

    def __str__(self):
        return f"{self.user.email}"



# Manager models
class Accountant(TimeStampUUIDModel):
    user = models.ForeignKey(User, related_name="accountants", on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, verbose_name=_("Employee ID"), blank=True, null=True)
    is_mobile_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="accountants/profile_pics", blank=True, verbose_name=_("Accountants Profile Image")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender = models.CharField(max_length=20, verbose_name=_("Gender"), choices=Gender.choices, default="--", blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 1"))
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 2"))
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"))
    about_me = models.TextField(blank=True, verbose_name=_("About Me"))
    salary = models.IntegerField(blank=True, null=True, verbose_name=_("Salary"))
    bank_account_details = models.TextField(blank=True, null=True, verbose_name=_("Bank Details"), )
    qualification = models.CharField(max_length=255, blank=True, verbose_name=_("Educational Qualification"))
    work_experience = models.CharField(max_length=75, blank=True, verbose_name=_("Work Experience"))
    status = models.BooleanField(default=False, verbose_name=_("Is Approved by Admin"))

    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_mobile(self):
        return self.user.mobile

    @property
    def get_user_id(self):
        return self.user.id

    @property
    def get_user_pkid(self):
        return self.user.pkid

    @property
    def get_user_role(self):
        if self.user.is_accountant:
            return f"Accountant"

    def __str__(self):
        return f"{self.user.email}"


# Manager models
class Salesman(TimeStampUUIDModel):
    user = models.ForeignKey(User, related_name="salesmen", on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, verbose_name=_("Employee ID"), blank=True, null=True)
    is_mobile_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="salesmen/profile_pics", blank=True, verbose_name=_("Salesman Profile Image")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender = models.CharField(max_length=20, verbose_name=_("Gender"), choices=Gender.choices, default="--", blank=True)
    address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 1"))
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Address Line 2"))
    city = models.CharField(max_length=255, blank=True, verbose_name=_("City"))
    state = models.CharField(max_length=255, blank=True, verbose_name=_("State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"))
    about_me = models.TextField(blank=True, verbose_name=_("About Me"))
    salary = models.IntegerField(blank=True, null=True, verbose_name=_("Salary"))
    bank_account_details = models.TextField(blank=True, null=True, verbose_name=_("Bank Details"), )
    qualification = models.CharField(max_length=255, blank=True, verbose_name=_("Educational Qualification"))
    work_experience = models.CharField(max_length=75, blank=True, verbose_name=_("Work Experience"))
    status = models.BooleanField(default=False, verbose_name=_("Is Approved by Admin"))

    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_mobile(self):
        return self.user.mobile

    @property
    def get_user_id(self):
        return self.user.id

    @property
    def get_user_pkid(self):
        return self.user.pkid

    @property
    def get_user_role(self):
        if self.user.is_salesman:
            return f"Salesman"

    def __str__(self):
        return f"{self.user.email}"



# Customer Model
class Customer(TimeStampUUIDModel):
    user = models.ForeignKey(User, related_name="customers", on_delete=models.CASCADE)
    proprietors_name = models.CharField(max_length=20, verbose_name=_("Proprietors Name"), blank=True)
    is_mobile_verified = models.BooleanField(default=False, verbose_name=_("Mobile Verified"))
    profile_picture = models.ImageField(
        default="default.jpg", upload_to="customers/profile_pics", blank=True, verbose_name=_("Customer Profile Image")
    )
    date_of_birth = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    gender = models.CharField(max_length=20, verbose_name=_("Gender"), choices=Gender.choices, default="--", blank=True)
    business_address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Business Address Line 1"))
    business_address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Business Address Line 2"))
    business_city = models.CharField(max_length=255, blank=True, verbose_name=_("Business City"))
    business_state = models.CharField(max_length=255, blank=True, verbose_name=_("Business State"))
    residence_address_line_1 = models.CharField(max_length=255, blank=True, verbose_name=_("Residence Address Line 1"))
    residence_address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_("Residence Address Line 2"))
    residence_city = models.CharField(max_length=255, blank=True, verbose_name=_("Residence City"))
    residence_state = models.CharField(max_length=255, blank=True, verbose_name=_("Residence State"))
    country = models.CharField(max_length=255, blank=True, verbose_name=_("Country"))
    about_me = models.TextField(blank=True, verbose_name=_("About Customer"))
    verified_customer = models.BooleanField(default=False)
    gst_no = models.CharField(max_length=30, blank=True, verbose_name=_("GST No"))
    gst_certificate = models.FileField(upload_to='uploads/%Y/%m/%d/', blank=True, verbose_name=_("GST Certificate"))
    pan_no = models.CharField(max_length=30, blank=True, verbose_name=_("PAN No"))
    pan_certificate = models.FileField(upload_to=user_directory_path, blank=True, verbose_name=_("PAN Card"))
    adhaar_no = models.IntegerField(blank=True, default=0, verbose_name=_("Adhaar No"))
    adhaar_certificate = models.FileField(upload_to=user_directory_path, blank=True, verbose_name=_("Adhaar Certificate"))
    security_cheque = models.FileField(upload_to=user_directory_path, blank=True, verbose_name=_("Security Cheque"))
    visiting_card = models.FileField(upload_to=user_directory_path, blank=True, verbose_name=_("Visiting Card"))


    @property
    def get_full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    @property
    def get_email(self):
        return self.user.email

    @property
    def get_mobile(self):
        return self.user.mobile

    @property
    def get_user_id(self):
        return self.user.id

    @property
    def get_user_pkid(self):
        return self.user.pkid

    @property
    def get_user_role(self):
        if self.user.is_customer:
            return f"Customer"

    def __str__(self):
        return f"{self.user.email}"


