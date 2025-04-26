from django.db import models

# Create your models here.
# class CP_REPORT(models.Model):
from django.db import models


class Cpreport(models.Model):
    Date = models.DateField(primary_key=True)
    TIME = models.TimeField()
    Parameter = models.CharField(max_length=100)
    StationId = models.CharField(max_length=100, null=True, blank=True)
    EquipmentId = models.CharField(max_length=100, null=True, blank=True)
    Value = models.FloatField(null=True, blank=True)
    ConnectionStatus = models.IntegerField(null=True, blank=True)
    Location = models.CharField(max_length=100, null=True, blank=True)
    Tool = models.CharField(max_length=100, null=True, blank=True)



    class Meta:
        db_table = 'Cpreport'  # 👈 دقت کن که حروف بزرگ‌کوچک مهمه برای SQL Server
        managed = False

      
    
