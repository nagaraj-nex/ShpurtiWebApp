from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from django.db import models  
from django.contrib.auth.models import User
from django.urls import reverse


class Company_Data(models.Model):
    cid = models.AutoField(primary_key=True)
    Account_Name = models.CharField(max_length=500,default="",null = True)
    Company_Name = models.CharField(max_length=500,default="",null = True)  
    Website = models.CharField(max_length=500,default="",null = True) 
    Employee_size = models.CharField(max_length=500,default="",null = True)
    Employee_Range = models.CharField(max_length=500,default="",null = True)
    Industry = models.CharField(max_length=500,default="",null = True)  
    Address_1 = models.CharField(max_length=500,default="",null = True)
    Address_2 = models.CharField(max_length=500,default="",null = True)
    Address_3 = models.CharField(max_length=500,default="",null = True)
    City = models.CharField(max_length=500,default="",null = True)
    State = models.CharField(max_length=500,default="",null = True)
    Zip_Code = models.CharField(max_length=500,default="",null = True)
    Country = models.CharField(max_length=500,default="",null = True)
    First_Name = models.CharField(max_length=500,default="",null = True)
    Last_Name = models.CharField(max_length=500,default="",null = True)
    Job_Title = models.CharField(max_length=500,default="",null = True)
    LinkedIn_URL = models.CharField(max_length=500,default="",null = True)
    Public_Profile = models.CharField(max_length=500,default="",null = True)
    Prospect_City = models.CharField(max_length=500,default="",null = True)
    Prospect_State = models.CharField(max_length=500,default="",null = True)
    Prospect_Country = models.CharField(max_length=500,default="",null = True)
    Email_Id = models.EmailField(default="",null = True)
    Country_Code = models.CharField(max_length=500,default="",null = True)
    Contact_Num = models.CharField(max_length=500,default="",null = True)
    Direct_Number = models.CharField(max_length=500,default="",null = True)
    Business_Solution = models.CharField(max_length=500,default="",null = True)
    Revenue_link = models.CharField(max_length=500,default="",null = True)
    Revenue = models.CharField(max_length=500,default="",null = True)
    Company_Techology = models.CharField(max_length=500,default="",null = True)
    Additional_information = models.CharField(max_length=500,default="",null = True) 
    Company_Linkedin_URL = models.CharField(max_length=500,default="",null = True)
    Company_Type = models.CharField(max_length=500,default="",null = True)
    Company_Founded_Year = models.CharField(max_length=500,default="",null = True)
    Job_Url = models.CharField(max_length=500,default="",null = True)
    Job_Opening = models.IntegerField(default=0,null = True)
    Department = models.CharField(max_length=500,default="",null = True)
    
    class Meta:  
        db_table = "Data"  


class UserProfile(models.Model):
    uid = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    Username = models.CharField(max_length=100, null=True)
    First_Name = models.CharField(max_length=100, null=True)
    Last_Name = models.CharField(max_length=100, null=True)
    Email_Id = models.EmailField(default="",null = True)
    Pass1 = models.CharField(max_length=100, null=True)
    Pass2 = models.CharField(max_length=100, null=True)

    class Meta:  
        db_table = "Data1"

    def get_absolute_url(self):
        return reverse('profile', kwargs={'id': self.id})

class Login(models.Model):
    username = models.CharField(max_length=50)
    Fname = models.CharField(max_length=50)
    Lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=32)
    class Meta:
        db_table = "login"


#class UserProfile(models.Model):
    #uid = models.AutoField(primary_key=True)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='profile')
    #username = models.CharField(max_length=500,default="",null = True)
    #first_name = models.CharField(max_length=500,default="",null = True)
    #last_name = models.CharField(max_length=500,default="",null = True)
    #email = models.EmailField(max_length=500,default="",null = True)
    #password1 = models.CharField(max_length=500,default="",null = True)
    #password2 = models.CharField(max_length=500,default="",null = True)

    #def get_absolute_url(self):
       # return reverse('profile', kwargs={'id': self.id})

