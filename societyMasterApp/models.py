from django.db import models

# Create your models here.
class Society(models.Model):
    society_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    door_no = models.CharField(max_length=10, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    area_name = models.CharField(max_length=255, null=True, blank=True)
    mandal = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Active', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.society_name