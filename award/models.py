from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length =30,null=True)
    screenshot = models.ImageField(upload_to = 'images/',null=True)
    description = models.TextField(null=True)
    link = models.URLField()
    user = models.ForeignKey(User, null=True)

    def __str__(self):
        return self.name

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    class Meta:
        ordering = ["-id"]

    @classmethod
    def get_projects(cls):
        projects = cls.objects.all()
        return projects


class Profile(models.Model):
    name = models.CharField(max_length =30,null=True)
    profile_photo = models.ImageField(upload_to = 'pics/')
    bio = models.TextField(max_length=100,blank=True)
    user_id = models.OneToOneField(User,on_delete=models.CASCADE)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def save_user(self):
        self.save()

    @classmethod
    def search_user(cls,username):
        searched_user = User.objects.get(username = username)
        return searched_user

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    def __str__(self):
        return self.user.username
