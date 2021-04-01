from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    # Complete = 1
    # Remaining = 0
    # choices=(
    #     'Complete',Complete,
    #     'Remaining',Remaining
    # )
    user        = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    title       = models.CharField(max_length=100)
    desc        = models.TextField()
    complete    = models.BooleanField(default=False)
    date        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("home")
    
    class Meta:
        ordering = ['complete']