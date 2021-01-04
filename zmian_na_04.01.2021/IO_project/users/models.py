#  from django.db import models
# # from django_countries.fields import CountryField
#  from django.contrib.auth.models import AbstractUser, BaseUserManager
# # from django.contrib.postgres.fields import ArrayField


# # class CustomUser(AbstractUser, models.Model):
# #    # country = CountryField()
# #     email = models.EmailField(
# #         unique=True,
# #         max_length=254
# #     )

# #     birthDate = models.DateField()
# #     subscription = models.BooleanField(default=False)
# #     boughtMovies = ArrayField(models.IntegerField(
# #         null=True, blank=True), null=True, blank=True)
# #     #nearby_places_ids = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django_countries.fields import CountryField


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, models.Model):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    country = CountryField()
    birthDate = models.DateField(null=True)
    subscription = models.BooleanField(default=False)
    # boughtMovies = ArrayField(models.IntegerField(
    #     null=True, blank=True), null=True, blank=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
