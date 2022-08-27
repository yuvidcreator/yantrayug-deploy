from django.db import models
import datetime
from django.utils import timezone
from apps.accounts.models import User
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampUUIDModel
from apps.products.models import HB, HBT, HT, Product
from apps.profiles.models import Customer, Salesman
from yantrayugBackend.dependancies import path_and_rename
from django.dispatch import receiver
# Create your models here.


class BillStatus(models.TextChoices):
    INCOMPLETE = "Incomplete", _("Incomplete")
    COMPLETE = "Complete", _("Complete")



class DispchStatus(models.TextChoices):
    PENDING = "Pending", _("Pending")
    COMPLETED = "Completed", _("Completed")
    HOLD = "Hold", _("Hold")
    CANCEL = "Cancel", _("Cancel")


class RecievedStatus(models.TextChoices):
    INCOMPLETE = "Incomplete", _("Incomplete")
    COMPLETE = "Complete", _("Complete")


class PaymentMethod(models.TextChoices):
    COD = "Cash On Delivery", _("Cash On Delivery")
    ONLINE = "Online Mode", _("Online Mode")
    CHEQUE = "Cheque", _("Cheque")


class RatingChoices(models.TextChoices):
    GOOD = "Good", _("Good")
    AVERAGE = "Average", _("Average")
    POOR = "Poor", _("Poor")
    BAD = "BAD", _("BAD")


class ProductChoices(models.TextChoices):
    HBT = HBT, _("HBT")
    HB = HB, _("HB")
    HT = HT, _("HT")



class Invoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    invoiceNo = models.CharField(max_length=120, verbose_name=_("Invoice No"))
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name="customer_dispatch", verbose_name=_("Party Name"))
    product = models.ManyToManyField(Product, related_name=_("product_invoice"), verbose_name=_("Select Product"))

    class Meta:
        verbose_name=_("Invoice")
        verbose_name_plural=_("Invoices")
        db_table = "invoices"  # Table Na

    def __str__(self):
        return f"{self.invoiceNo} --> {self.customer}"





class Dispatch(models.Model):
    id = models.BigAutoField(primary_key=True)
    dispatchOrderID = models.CharField(max_length=50, editable=False)
    entryDate = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Time"))
    invoiceNo = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name="invoice_dispatch", verbose_name=_("Invoice No"))
    salesman = models.ForeignKey(Salesman, on_delete=models.PROTECT, related_name="salesman_custmrdispatch", verbose_name=_("Salesman Name"))
    pickList = models.PositiveIntegerField(default=0, blank=True, verbose_name=_("Pick List"))
    billStatus = models.CharField(max_length=255, verbose_name=_("Bill Status"), choices=BillStatus.choices, default=_("Select"))
    deliveredBoy = models.ForeignKey(Salesman, on_delete=models.PROTECT, blank=True, related_name="delivered_by", verbose_name=_("Delivered By"))
    deliveryDate = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name=_("Enter Delivery Date"))
    pickerName = models.ForeignKey(User, on_delete=models.PROTECT, related_name="picker_name", verbose_name=_("Picker Name"))
    dispatchStatus = models.CharField(max_length=120, verbose_name=_("Dispatch Status"), choices=DispchStatus.choices, default=_("Select Status"))
    recievedStatus = models.CharField(max_length=120, verbose_name=_("Recieved Status"), choices=RecievedStatus.choices, default=_("Select Status"))
    recievedImage = models.FileField(upload_to=path_and_rename, blank=True, verbose_name=_("Upload Recieved Image"))
    payment_method = models.CharField(max_length=100, blank=True, null=True, choices=PaymentMethod.choices, default="Select Payment Method", verbose_name=_("Payment Mode"))
    remark = models.CharField(max_length=255, verbose_name=_("Remark"), blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name=_("Dispatch")
        verbose_name_plural=_("Dispatches")
        db_table = "dispatches"  # Table Na

    def __str__(self):
        return f"{self.invoiceNo}"



class RecievedReciept(TimeStampUUIDModel):
    dispatch = models.ForeignKey(Dispatch, on_delete=models.PROTECT, verbose_name=_("Dispatch ID"))
    payment_method = models.CharField(max_length=100, blank=True, null=True, choices=PaymentMethod.choices, default="Select Payment Method", verbose_name=_("Payment Mode"))
    uploadReciept = models.FileField(upload_to=path_and_rename, blank=True, verbose_name=_("Upload Recieved Image/File"))
    recivedStatus = models.CharField(max_length=120, verbose_name=_("Recieved Status"), choices=RecievedStatus.choices, default=_("Select Status"))
    locationLink = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Google Map Link"))
    latitude = models.FloatField(default=19.214, blank=True, verbose_name=_("Set Latitude"))
    longitude = models.FloatField(default=19.214, blank=True, verbose_name=_("Set Longitude"))
    area_name = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Area Name"))
    landmark = models.CharField(max_length=64, null=True, blank=True, verbose_name=_("Landmark"))
    remarks = models.CharField(max_length=255, verbose_name=_("Remark"), blank=True)
    ratings = models.CharField(max_length=255, choices=RatingChoices.choices, verbose_name=_("Ratings"), blank=True)
    uploadedAt = models.DateTimeField(auto_now_add=True, verbose_name=_("Uploaded At"))

    def __str__(self):
        return f"{self.dispatch.invoiceNo} --> {self.recivedStatus}"




@receiver(models.signals.post_save, sender=Dispatch)
def generate_custom_oredr_id(sender, instance, created, **kwargs):

    if created:
        date_format = instance.created_at.strftime("%d%m")
        instance.dispatchOrderID = f"""{instance.invoiceNo.invoiceNo.upper()}{date_format}{10000+instance.id}"""
        instance.save()
    else:
        # if instance.booking_status == "booking_cancelled":
        #     jobs = instance.booking_order_schedules.all()
        #     if jobs.exists():
        #         jobs.delete()
        pass