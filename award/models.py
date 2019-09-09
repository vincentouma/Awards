from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    link = models.CharField(max_length=100)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='project_pics',blank=True)
    user_project_id = models.IntegerField(default=0)
    design = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    usability = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    content = models.IntegerField(choices=list(zip(range(0, 11), range(0, 11))), default=0)
    vote_submissions = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']

    def save_project(self):
        self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def fetch_all_images(cls):
        all_images = Project.objects.all()
        return all_images

    @classmethod
    def search_project_by_title(cls,search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

    @classmethod
    def get_single_project(cls, project):
        project = cls.objects.get(id=project)
        return project

    class Meta:
        ordering = ['-id']


class Profile(models.Model):
    profile_picture = models.ImageField(upload_to='prof_pics/',blank=True)
    prof_user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bio = models.TextField(default="")
    contact_info = models.CharField(max_length=200,blank=True)
    profile_Id = models.IntegerField(default=0)
    all_projects = models.ForeignKey('Project',on_delete=models.CASCADE,null=True)

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
    post =  models.ForeignKey(Project,on_delete=models.CASCADE,related_name='likes')
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

    def __str__(self):
        return self.comment

    def save_comment(self):
            self.save()

    def delete_comment(self):
        self.delete()

    class Meta:
        ordering = ["-id"]

        
                