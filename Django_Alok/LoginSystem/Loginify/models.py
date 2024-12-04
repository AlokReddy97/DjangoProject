from django.db import models

class UserDetails(models.Model):
    email = models.EmailField(primary_key=True, unique=True)  # Email as primary key
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=12, blank=True)

    def __str__(self):
        return self.email  # Return email as it is now the primary key
