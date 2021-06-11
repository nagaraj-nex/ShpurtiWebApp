from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from django.db import models  


class Company_Data(models.Model):
    cid = models.AutoField(primary_key=True)
    Company_Name = models.CharField(max_length=500,default="",null = True)  
    Website = models.CharField(max_length=500,default="",null = True) 
    Employee_Range = models.IntegerField(default=0,null = True)
    Industry = models.CharField(max_length=500,default="",null = True)  
    Address_1 = models.CharField(max_length=500,default="",null = True)
    Address_2 = models.CharField(max_length=500,default="",null = True)
    City = models.CharField(max_length=500,default="",null = True)
    Zip_Code = models.CharField(max_length=500,default="",null = True)
    Country = models.CharField(max_length=500,default="",null = True)
    First_Name = models.CharField(max_length=500,default="",null = True)
    Last_Name = models.CharField(max_length=500,default="",null = True)
    Job_Title = models.CharField(max_length=500,default="",null = True)
    LinkedIn_URL = models.CharField(max_length=500,default="",null = True)
    Public_Profile = models.CharField(max_length=500,default="",null = True)
    Email_Id = models.EmailField(default="",null = True)
    Contact_Num = models.IntegerField(default=0,null = True)
    Job_Url = models.CharField(max_length=500,default="",null = True)
    Job_Opening = models.IntegerField(default=0,null = True)
    
    
    class Meta:  
        db_table = "Data"  


