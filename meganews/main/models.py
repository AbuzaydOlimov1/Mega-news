from django.db import models


class Category(models.Model):
    photo = models.ImageField()
    name = models.CharField(max_length=255)


class Ad(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Post(models.Model):
    photo = models.ImageField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    date = models.DateField()


class Latestvideo(models.Model):
    video =models.URLField()
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Handbook(models.Model):
    mega_news = models.TextField()
    newsletter = models.EmailField()
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    insta = models.URLField()
    twitter = models.URLField()


class Comment(models.Model):
    name = models.CharField(max_length=255)
    text = models.CharField(max_length=255)


class Insta(models.Model):
    photo = models.ImageField()
    link = models.URLField()


class Login(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Postinfo(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField()
    date = models.DateField()
    text = models.TextField()


class Sendpost(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    explanation = models.TextField()
    photo = models.ImageField()


class Sendvideo(models.Model):
    title = models.CharField(max_length=255)
    tags = models.CharField(max_length=255)
    explanation = models.TextField()
    video = models.URLField()


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    location = models.URLField()
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Team(models.Model):
    photo = models.ImageField()
    job = models.CharField(max_length=255)
    name = models.CharField(max_length=255)


class Contactus(models.Model):
    subject = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    explantion = models.TextField()
    file = models.FileField()