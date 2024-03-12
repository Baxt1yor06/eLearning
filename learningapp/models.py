from django.urls     import reverse
from django.db import models

# Create your models here.

class Index_carousel(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    img = models.ImageField(upload_to='index_carousel/')
    slug = models.SlugField(max_length=200)
    def get_absolute_url(self):
        return reverse("detail1", args=[self.slug])
    def __str__(self):
        return self.name
    

class Skils(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self):
        return self.name


class About(models.Model):
    name1 = models.CharField(max_length=300)
    bio = models.TextField()
    skils1= models.CharField(max_length=300)
    skils2 = models.CharField(max_length=300)
    skils3 = models.CharField(max_length=300)
    skils4 = models.CharField(max_length=300)
    skils5 = models.CharField(max_length=300)
    skils6 = models.CharField(max_length=300)
    img = models.ImageField(upload_to='about/')
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("detail3", args=[self.slug])
    
    def __str__(self):
        return self.name1


class Courses(models.Model):
    name = models.CharField(max_length=200)
    courses = models.IntegerField()
    img = models.ImageField(upload_to='courses/')
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("detail4", args=[self.slug])

    def __str__(self):
        return self.name


class Popular_courses(models.Model):
    name = models.CharField(max_length=300)
    person_name = models.CharField(max_length=200)
    time = models.TimeField()
    students = models.IntegerField()
    img = models.ImageField(upload_to='pupular_courses/')
    price = models.IntegerField()
    slug = models.SlugField()


    def get_absolute_url(self):
        return reverse("detail5", args=[self.slug])

    def __str__(self):
        return self.name


class Instructors(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    img = models.ImageField(upload_to='instructors/')
    slug = models.SlugField()


    def get_absolute_url(self):
        return reverse("detail6", args=[self.slug])

    def __str__(self):
        return self.name

class Clients(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    profession = models.CharField(max_length=200)
    img = models.ImageField(upload_to='clients/')
    slug = models.SlugField()

    def get_absolute_url(self):
        return reverse("detail7", args=[self.slug])

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

