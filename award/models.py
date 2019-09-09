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
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField(default="")
    contact_info = models.CharField(max_length=200,blank=True)
    profile_Id = models.IntegerField(default=0)
    all_projects = models.ForeignKey('Projects',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_bio(self,bio):
        self.bio = bio
        self.save()

class Rates(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post =  models.ForeignKey(Projects,on_delete=models.CASCADE,related_name='likes')
    design = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    usability = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)],null=True)
    creativity = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
    content = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(10)])
git 
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

        
                