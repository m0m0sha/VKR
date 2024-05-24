from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(username=username, **extra_fields)
        if password:
            user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user


class Survey(models.Model):
    hours = models.IntegerField()
    enoughSleep = models.IntegerField()
    tiredness = models.IntegerField()
    quality = models.IntegerField()
    fallingAspleep = models.IntegerField()
    nightWaking = models.IntegerField()
    electronicDevices = models.IntegerField()
    routine = models.IntegerField()
    caffeine = models.IntegerField()
    refreshed = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super(Survey, self).__init__(*args, **kwargs)


class CourseDay(models.Model):
    daynumber = models.IntegerField()
    surveyid = models.ForeignKey(Survey, on_delete=models.SET_NULL, null=True, blank=True)
    userid = models.IntegerField()
    done = models.BooleanField(default=False)

    def __init__(self, *args, **kwargs):
        super(CourseDay, self).__init__(*args, **kwargs)


class User(AbstractUser):
    virtual_balance = models.IntegerField(default=0)
    game_money_balance = models.IntegerField(default=0)
    currentDay = models.ForeignKey(CourseDay, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.first_name


class Course(models.Model):
    paragraphs = models.JSONField()  # Массив строк для абзацев

    def __init__(self, *args, **kwargs):
        super(Course, self).__init__(*args, **kwargs)
