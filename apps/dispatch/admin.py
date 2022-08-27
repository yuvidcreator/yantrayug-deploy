from django.contrib import admin
from apps.dispatch.models import *
from django.contrib.auth.models import Group, Permission




admin.site.register(Invoice)



@admin.register(Dispatch)
class DispatchAdmin(admin.ModelAdmin):
    search_fields = ['invoiceNo']
    # readonly_fields = ["propertyStatus","isPropertyActive"]
    list_display = [
        "entryDate",
        "invoiceNo",
        "billStatus",
        "deliveredBoy",
        "deliveryDate",
        "dispatchStatus",
        "recievedStatus",
        "created_at",
        "updated_at",
    ]



@admin.register(RecievedReciept)
class RecievedRecieptAdmin(admin.ModelAdmin):
    search_fields = ['dispatch']
    # readonly_fields = ["propertyStatus","isPropertyActive"]
    list_display = [
        "dispatch",
        "payment_method",
        "recivedStatus",
        "uploadedAt",
        "uploadReciept",
    ]







# def get_readonly_fields(self, request, obj=None):
#         if Group.objects.filter(name = "draft_publish_group").filter(user__id = request.user.id).exists() or request.user.is_superuser:
#             return []
#         return self.readonly_fields