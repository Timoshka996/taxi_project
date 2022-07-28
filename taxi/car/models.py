from django.db import models


class Email(models.Model):
    pochta = models.EmailField(blank=True, null=True)


class Join(models.Model):
    car_type = models.CharField(max_length=250)
    car_tip = models.CharField(max_length=250)
    car_size = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.car_tip}, {self.car_type}, {self.car_size}"

    

    

    

    
