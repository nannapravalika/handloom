from django.db import models
from weaverApp.models import WeaverDetail

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# class Indent(models.Model):
#     indent_no = models.CharField(max_length=50)
#     date = models.DateField()
#     qty = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     gst_percent = models.DecimalField(max_digits=5, decimal_places=2)
#     gst_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     net_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     status = models.CharField(max_length=20)
#     weaver = models.ForeignKey(WeaverDetail, on_delete=models.CASCADE)
#     tender_no = models.CharField(max_length=50)

#     def __str__(self):
#         return self.indent_no