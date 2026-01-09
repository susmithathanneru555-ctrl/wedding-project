from django.db import models
class Invitation(models.Model):
    groom_name = models.CharField(max_length=100)
    bride_name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    well_wisher=models.CharField(max_length=100)
    wedding_date = models.DateField()
    venue = models.CharField(max_length=200)
    address = models.TextField()
    buffet_details = models.TextField()

    def __str__(self):
        return f"{self.groom_name} & {self.bride_name} Wedding Invitation"