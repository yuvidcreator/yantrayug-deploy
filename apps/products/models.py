from django.db import models

import datetime
from django.utils import timezone
import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampUUIDModel
from yantrayugBackend.dependancies import path_and_rename

# Create your models here.


class ProductTypes(models.TextChoices):
    HERO = "Hero", _("Hero")
    BATTERY = "Battery", _("Battery")
    TYRE = "Tyre", _("Tyre")


class ProductImages(TimeStampUUIDModel):
    product = models.ForeignKey("Product", on_delete=models.CASCADE, verbose_name=_("Select Product Name"))
    image = models.ImageField(upload_to="products_images/{product.typeOfProduct}", blank=True, verbose_name=_("Set Image (1920 x 1280px)"), help_text=_("Image size should be 1920 x 1280px"))





class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    productId = models.CharField(max_length=50, editable=False)
    name = models.CharField(max_length=120, blank=True, verbose_name=_("Product Name"))
    partNo = models.CharField(max_length=120, blank=True, verbose_name=_("Part No"))
    brand = models.CharField(max_length=120, blank=True, verbose_name=_("Brand"))
    typeOfProduct = models.CharField(max_length=255, choices=ProductTypes.choices, default="Select Type", verbose_name=_("Product Type"))
    capacity = models.CharField(max_length=5, blank=True, default=0.0, verbose_name=_("Battery Capacity"), help_text="If Product is Battery Please fill Capacity, otherwise Leave Blank")
    description = models.CharField(max_length=255, blank=True, verbose_name=_("Description"))
    sku = models.CharField(max_length=120, blank=True, verbose_name=_("SKU"))
    mainImage = models.ImageField(
        default="default.jpg",
        upload_to="products_images/{product.typeOfProduct}",
        blank=True,
        verbose_name=_("Hero Image"),
    )
    price = models.PositiveBigIntegerField(default=0, verbose_name=_("Price"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name=_("Product")
        verbose_name_plural=_("Products")
        db_table = "products"  # Table Name

    def __str__(self):
        return self.name






class HBT(TimeStampUUIDModel):
    product = models.ManyToManyField(Product, related_name="product_hbt", verbose_name=_("HBT"))

    class Meta:
        verbose_name=_("Hero Battery Tyre")
        verbose_name_plural=_("HBTs")
        db_table = "hbts"  # Table Na

    def __str__(self):
        return f"{self.hero} + {self.battery} + {self.tyre}"


class HB(TimeStampUUIDModel):
    product = models.ManyToManyField(Product, related_name="product_hb", verbose_name=_("HB"))

    class Meta:
        verbose_name=_("Hero Battery")
        verbose_name_plural=_("HBs")
        db_table = "hbs"  # Table Na

    def __str__(self):
        return f"{self.hero} + {self.battery}"


class HT(TimeStampUUIDModel):
    product = models.ManyToManyField(Product, related_name="product_ht", verbose_name=_("HT"))

    class Meta:
        verbose_name=_("Hero Tyre")
        verbose_name_plural=_("HTs")
        db_table = "hts"  # Table Na

    def __str__(self):
        return f"{self.hero} + {self.tyre}"


