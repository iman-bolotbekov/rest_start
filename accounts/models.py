from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    name = models.CharField(max_length=30)
    birth_date = models.DateField()
    registered_date = models.DateField()
    phone_number = models.CharField(max_length=12)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




