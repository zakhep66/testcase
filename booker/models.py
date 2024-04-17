# books/models.py

from django.db import models

from booker.tasks import notify_users_about_new_book


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="media/books/", null=True, blank=True)

    def __str__(self):
        return self.title
