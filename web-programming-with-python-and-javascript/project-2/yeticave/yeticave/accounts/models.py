from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = None
    last_name = None

    email: str = models.EmailField("Email Address", unique=True)