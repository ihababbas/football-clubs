from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.models import CustomUser


class Team(models.Model):
    team_name = models.CharField(max_length=56)
    country_name = models.CharField(max_length=56) 
    team_color = models.CharField(max_length=56)
    #logo = models.ImageField(upload_to='upload/', default="")
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return self.country_name

    def get_absolute_url(self):
        return reverse("detail_view", args=[self.id])
    
    class Meta:
        verbose_name_plural = "Teams"