

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=50)

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.second_name)


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return "{name}".format(name=self.name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)
    isbn = models.CharField(max_length=17)
    publisher = models.ForeignKey(Publisher)

    def __str__(self):
        return "{title} {author}".format(title=self.title, author=self.author)
