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


class Rates(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post =  models.ForeignKey(Projects,on_delete=models.CASCADE,related_name='likes')
    design = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)],null=True)
    creativity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    content = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])

    def save_rate(self):
            self.save()

    def delete_rate(self):
        self.delete()

class Comment(models.Model):
    comment = models.CharField(max_length =80,null=True)
    user = models.ForeignKey(User,null=True)
    project = models.ForeignKey(Projects,related_name='comments',null=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
            self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        ordering = ["-id"]

        
                