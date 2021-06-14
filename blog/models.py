from django.db import models

# Create your models here.

# Create A Blog models
# title
# pub_date
# body
# image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# Add the blog app to the settings

# create a migration

# Migrate

# add to the admin
