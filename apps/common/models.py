from django.db import models
import uuid
import datetime
from datetime import datetime
from django.utils import timezone
from django.utils.crypto import get_random_string
# Create your models here.





class TimeStampUUIDModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    pkid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True