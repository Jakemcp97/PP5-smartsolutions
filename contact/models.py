from django.db import models

# Create your models here.


class Contact(models.Model):

    class Meta:
        """"
        Allows you to have a user friendly name.
        """

        verbose_name_plural = 'Customer Enquiries'

    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=False, blank=False)
    order_number = models.CharField(max_length=50, null=False, blank=True)
    message = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return self.email
