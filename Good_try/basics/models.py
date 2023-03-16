from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Data(models.Model):
    title = models.TextField(blank=True, null=True)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        blank=True,
        null=True
    )
    accommodation_type = models.CharField(max_length=20, null=True, blank=True)
    img_url = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    contact_phone = models.CharField(max_length=100, null=True, blank=True)
    contact_email = models.CharField(max_length=100, null=True, blank=True)
    free = models.BooleanField(default=True)

    class Meta:
        ordering = ['-pub_date']
