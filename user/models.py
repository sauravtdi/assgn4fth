from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import string
import random
import pytz
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, email, full_name=None, password=None, timezone=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("users must have an email address")
        if not full_name:
            raise ValueError("users must have a name")
        if not password:
            raise ValueError("users must have a password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)  # change user password
        user_obj.full_name = full_name
        user_obj.timezone = timezone
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, full_name, password=None, timezone=None):

        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            timezone=timezone,
            is_staff=True
        )
        return user

    def create_superuser(self, email, full_name, password=None, timezone=None):

        user = self.create_user(
            email,
            full_name=full_name,
            password=password,
            timezone=timezone,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    id = models.SlugField(primary_key=True, unique=True,
                          editable=False, blank=True)
    full_name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)  # can login
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)  # superuser
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
    timezone = models.CharField(max_length=60, choices=TIMEZONES,
                                default='UTC', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']

    class Meta:
        db_table = 'user'

    def save(self, *args, **kwargs):
        while not self.id:
            newslug = ''.join([
                "W",
                "".join(random.sample(string.digits, 2)),
                "".join(random.sample(string.ascii_uppercase, 2)),
                "".join(random.sample(string.digits, 2)),
                "".join(random.sample(string.ascii_uppercase, 2)),
            ])

            if not type(self).objects.filter(pk=newslug).exists():
                self.id = newslug

        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.email
    objects = UserManager()

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin():
        return self.admin

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class ActivityPeriod(models.Model):
    activity_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='activity_periods', on_delete=models.CASCADE,
                             null=False, blank=True, verbose_name='the assigned user',)
    start_time = models.DateTimeField(editable=True)
    end_time = models.DateTimeField(editable=True)

    def __str__(self):
        return str(self.activity_id)

    def save(self, *args, **kwargs):
        if self.start_time > self.end_time:
            raise ValidationError(
                {"end_time": "finish must occur after start"})
        return super(ActivityPeriod, self).save(*args, **kwargs)

    class Meta:
        db_table = 'activity_period'
