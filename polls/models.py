from django.db import models

# Create your models here.
class Filial(models.Model):
    code = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    filtype = models.CharField(max_length=250, blank=True, null=True)
    federation_subject = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    street = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
    worktime = models.CharField(max_length=250, blank=True, null=True)
    geocode = models.CharField(max_length=100, blank=True, null=True)   
    

    class Meta:
        db_table = 'import_filial'

#CREATE TABLE "import_filial" ( `code` TEXT, `name` TEXT, `type` TEXT, `federation_subject` TEXT, 
# `city` TEXT, `street` TEXT, `number` TEXT, `worktime` TEXT, `geocode` TEXT )