from django.db import models

# Create your models here.
class WeaverDetail(models.Model):
    photo = models.CharField(max_length=255, null=True, blank=True)
    weaver_name = models.CharField(max_length=255, null=True, blank=True)
    society_name = models.CharField(max_length=255)
    master_weaver_name = models.CharField(max_length=255)
    weaver_code = models.CharField(max_length=255)
    weaver_card = models.CharField(max_length=255, null=True, blank=True)
    ration_card = models.CharField(max_length=255, null=True, blank=True)
    nhdc_passbook = models.CharField(max_length=255, null=True, blank=True)
    aadhar_card = models.CharField(max_length=255)
    bank_name = models.CharField(max_length=255, null=True, blank=True)
    account_no = models.CharField(max_length=255, null=True, blank=True)
    ifsc_code = models.CharField(max_length=255, null=True, blank=True)
    branch_name = models.CharField(max_length=255, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    relationship = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    door_no = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    area_name = models.CharField(max_length=255, null=True, blank=True)
    mandal = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    mobile_no = models.CharField(max_length=20, null=True, blank=True)
    payment = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    signature = models.CharField(max_length=255, null=True, blank=True)
    no_of_charkas = models.IntegerField(null=True, blank=True)
    no_of_looms = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=50, default='Active', null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.weaver_name