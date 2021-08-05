from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from.models import Company_Data, UserProfile,Login
#from.models import Login

admin.register(Company_Data)

class Company_DataAdmin(ImportExportModelAdmin):
    list_display = ('cid','Company_Name','Website','Employee_Range','Industry','Address_1',
    'Address_2','City','Zip_Code','Country','First_Name','Last_Name','Job_Title','LinkedIn_URL','Public_Profile',
    'Email_Id','Contact_Num','Job_Url','Job_Opening')
    
admin.site.register(Company_Data)
admin.site.register(UserProfile)
admin.site.register(Login)