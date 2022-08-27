from django.contrib import admin
from apps.products.models import *
# Register your models here.



class TabularInlineBase(admin.TabularInline):
    list_per_page = 2

class ProductsImagesInline(TabularInlineBase):
    model = ProductImages

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['name', 'typeOfProduct', 'sku']
    # readonly_fields = ["propertyStatus","isPropertyActive"]
    list_display = [
        "id",
        "name",
        "typeOfProduct",
        "sku",
        "price",
        "created_at",
        "updated_at",
        # "owner",
        # "isPropertyActive",
        # "created_at",
        # "updated_at",
        # "cover_image",
        # "country",
        # "description",
        # "map_image"
        # "explain_why_different",
    ]
    inlines = [ProductsImagesInline]



admin.site.register(HBT)
admin.site.register(HB)
admin.site.register(HT)