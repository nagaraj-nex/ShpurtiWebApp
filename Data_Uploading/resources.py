from django.db import models
from import_export import resources
from .models import Company_Data
#from import_export import resources

class Company_DataReasources(resources.ModelResource):
    class meta:
        models = Company_Data
