# Django imports
from django.contrib.auth.models import AbstractBaseUser
from .base_manager import MyAccountManager
from django.db import models
import uuid
from setup.basemodel import BaseModel
from datetime import datetime
from django.utils import timezone


# USER BASIC MODELS
class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)
    username = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)

    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=10, unique=True)


    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last joined", auto_now=True)
    last_seen = models.DateTimeField(verbose_name="last seen", blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = MyAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name_plural = "Users"
        ordering = ["first_name"]

    def __str__(self):
        if self.first_name:
            return self.get_full_name()
        return self.phone_number

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        return self.first_name or "Anonymous"

    def initials(self):
        if self.first_name and self.last_name:
            return f"{(self.first_name[0] + self.last_name[0]).upper()}"
        return self.email[0].upper()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    def age(self):
        from datetime import date

        if self.date_of_birth:
            return date.today().year - self.date_of_birth.year
        return None

    def set_fcm_token(self, token):
        self.fcm_token = token
        self.save()

    def get_fcm_token(self):
        return self.fcm_token


class LoggedInUserDevices(BaseModel):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="logged_in_user_user"
    )
    ip_address = models.GenericIPAddressField()
    os = models.CharField(max_length=255)
    browser = models.CharField(max_length=255)
    expires = models.DateTimeField(default=datetime.utcnow)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.get_full_name()}-{self.ip_address}"

    def is_refresh_token_expired(self):
        return datetime.utcnow().day >= self.created_at.day + 1

    class Meta:
        ordering = ["-created_at"]

