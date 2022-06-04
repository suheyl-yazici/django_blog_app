from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=50,blank=True,null=True)
    # email = models.EmailField(blank=True,null=True)
    image = models.ImageField(upload_to="media/", blank=True, default="media/indir.png")
    bio = models.TextField(blank=True)

    def _str_(self):
        return self.username
