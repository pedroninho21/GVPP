from django.db import models
import datetime
from django.contrib.auth import get_user_model

User = get_user_model()




class Used_Car(models.Model):

    title = models.CharField(max_length=50, verbose_name="Car Title", null=False)
    short_intro = models.CharField(max_length=100, verbose_name='Short Intro (max 100 characters)')
    car_img = models.ImageField(default='', upload_to='used_cars', verbose_name="Car Image", null=False)
    price = models.IntegerField(default=0, null=True)
    description = models.TextField()
    availability = models.BooleanField(default=True, verbose_name='Is Available')
    model = models.CharField(max_length=50, null=True)
    last_modified = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Last Edited on')

    def __str__(self):

        return self.title





class Service(models.Model):

    service_name = models.CharField(max_length=50, verbose_name='Service Name', null=False)
    availability = models.BooleanField(default=True, verbose_name='Service is Available')
    service_intro = models.CharField(max_length=120, verbose_name='Service Intro( max 120 characters )', null=False)
    service_description = models.TextField(null=False)
    service_icon = models.ImageField(default='', null=False, upload_to='service_icons')


    def __str__(self):

        return self.service_name
        

class Opening_Hours(models.Model):

    opening_time = models.CharField(max_length=50, verbose_name='Opening Time',choices=(('1 AM', '1 AM'),
                                                                                          ('2 AM', '2 AM'),
                                                                                          ('3 AM', '3 AM'),
                                                                                          ('4 AM', '4 AM'),
                                                                                          ('5 AM', '5 AM'),
                                                                                          ('6 AM', '6 AM'),
                                                                                          ('7 AM', '7 AM'),
                                                                                          ('8 AM', '8 AM'),
                                                                                          ('9 AM', '9 AM'),
                                                                                          ('10 AM', '10 AM'),
                                                                                          ('11 AM', '11 AM'),
                                                                                          ('12 AM', '12 AM'),
                                                                                          ('1 PM', '1 PM'),
                                                                                          ('2 PM', '2 PM'),
                                                                                          ('3 PM', '3 PM'),
                                                                                          ('4 PM', '4 PM'),
                                                                                          ('5 PM', '5 PM'),
                                                                                          ('6 PM', '6 PM'),
                                                                                          ('7 PM', '7 PM'),
                                                                                          ('8 PM', '8 PM'),
                                                                                          ('9 PM', '9 PM'),
                                                                                          ('10 PM', '10 PM'),
                                                                                          ('11 PM', '11 PM'),
                                                                                          ('12 PM', '12 PM'),
                                                                                          ), 
                                                                                          null=False)

    closing_time = models.CharField(max_length=50,null=True, verbose_name='Closing Time',choices=(('1 AM', '1 AM'),
                                                                                          ('2 AM', '2 AM'),
                                                                                          ('3 AM', '3 AM'),
                                                                                          ('4 AM', '4 AM'),
                                                                                          ('5 AM', '5 AM'),
                                                                                          ('6 AM', '6 AM'),
                                                                                          ('7 AM', '7 AM'),
                                                                                          ('8 AM', '8 AM'),
                                                                                          ('9 AM', '9 AM'),
                                                                                          ('10 AM', '10 AM'),
                                                                                          ('11 AM', '11 AM'),
                                                                                          ('12 AM', '12 AM'),
                                                                                          ('1 PM', '1 PM'),
                                                                                          ('2 PM', '2 PM'),
                                                                                          ('3 PM', '3 PM'),
                                                                                          ('4 PM', '4 PM'),
                                                                                          ('5 PM', '5 PM'),
                                                                                          ('6 PM', '6 PM'),
                                                                                          ('7 PM', '7 PM'),
                                                                                          ('8 PM', '8 PM'),
                                                                                          ('9 PM', '9 PM'),
                                                                                          ('10 PM', '10 PM'),
                                                                                          ('11 PM', '11 PM'),
                                                                                          ('12 PM', '12 PM'),
                                                                                          ),
                                                                                          )

    last_modified_date = models.DateTimeField(default=datetime.datetime.now(), verbose_name='Last Modified')



    



