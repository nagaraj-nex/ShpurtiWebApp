from django import forms  
from. models import Company_Data  

class Company_DataForm(forms.ModelForm):  
    class Meta:  
        model = Company_Data  
        fields = "__all__"  