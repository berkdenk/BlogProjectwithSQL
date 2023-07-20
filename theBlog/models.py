from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

class Category(models.Model):
    name=models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
    
    
class Post(models.Model):
    title=models.CharField(max_length=255)
    title_tag=models.CharField(max_length=255,default="Blog Site")
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    #silinen kullanıcının postunun silinmesi için
    body=models.TextField()
    post_date=models.DateField(auto_now_add=True)
    category=models.CharField(max_length=255,default="coding")
    likes=models.ManyToManyField(User,related_name='blog_posts')

    def __str__(self):
        return self.title +' | ' + str(self.author) 
        #page title and author not wierd numbers

    def get_absolute_url(self):
        return reverse('home')
    
    