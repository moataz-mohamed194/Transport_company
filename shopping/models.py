import datetime
from django.db import models


class LoadData(models.Model):
    driver = models.CharField(  
                                default="", 
                                max_length=300,
                                blank=True, null=True,
                                verbose_name="اسم السائق")
    number_of_car = models.CharField(
                                null=True, 
                                blank=True,
                                max_length=100,
                                verbose_name="رقم العربية")
    date_of_get_in = models.DateField(
                                null=True, 
                                blank=True, 
                                verbose_name="تاريخ الدخول")
    date_of_get_out = models.DateField(
                                null=True, 
                                blank=True, 
                                verbose_name="تاريخ الخروج")
    load = models.TextField(
                                verbose_name='الحمولة',
                                blank=True,
                                null=True
    )
    added_data = models.CharField(  
                                default="", 
                                max_length=300,
                                blank=True, null=True,
                                verbose_name="اسم مدخل البيانات")
    edited_data = models.CharField(
                                default="",
                                max_length=300,
                                blank=True, null=True,
                                verbose_name="اسم القائم بالتعديل")
    
    def __str__(self):
        return self.number_of_car

    class Meta:
        verbose_name =  'بيانات الحمولة'
        verbose_name_plural =  'بيانات الحمولة'


def regex_transform(regex_string: str):

    """ takes an OracleDB format regex string and returns a PostgreSQL regex string"""
    regex_string = regex_string.strip().replace('\\', '')
    regex_string = regex_string.replace('/', '')
    regex_string = regex_string.replace('%', '.*')
    return regex_string
