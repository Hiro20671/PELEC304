from django.db import models

class Enrollment(models.Model):
    full_name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
