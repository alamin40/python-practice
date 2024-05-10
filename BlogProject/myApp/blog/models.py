from unicodedata import category
from django.db import models

# Create your models here.


# Category model
class Category(models.Model):
  cat_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=100)
  description = models.TextField()
  url = models.CharField(max_length=100)
  image = models.ImageField(upload_to='category/')
  add_date = models.DateField(auto_now_add=True, null=True)
  

# Post model  
class Post(models.Model):
  post_id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  content = models.TextField()
  url = models.CharField(max_length=100)
  cat = models.ForeignKey(Category, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='post/')