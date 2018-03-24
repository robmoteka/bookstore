from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    second_name = models.CharField(max_length=50)

    def __str__(self):
        return "{first} {last}".format(first=self.first_name, last=self.second_name)


class Publisher(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return "{name}".format(name=self.name)


class BookCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Books nonphysical item
    """
    title = models.CharField(verbose_name=_("Book title"), max_length=100)
    categories = models.ManyToManyField(BookCategory)
    authors = models.ManyToManyField(Author, verbose_name="Authors")

    # author = models.ForeignKey(Author)
    def get_author(self):
        """
        Used in admin.py to display property lists of authors

        :return:
        Returns joined string  - first and last name for all book authors divided by comma
        """
        
        return ", ".join([a.first_name + " " + a.second_name for a in self.authors.all()])

    def __str__(self):
        return "{title} {author}".format(title=self.title, author=self.authors)


class BookEdition(models.Model):
    """
    Wydanie
    """
    book = models.ForeignKey(Book)
    publisher = models.ForeignKey(Publisher)
    date = models.DateField()
    isbn = models.CharField(max_length=17)

    def __str__(self):
        return "{book.title}, {publisher.name} ".format(book=self.book, publisher=self.publisher)


COVER_TYPES = (
    ('soft', 'Soft'),
    ('hard', 'Hard'),
    # wartość w bazie, wartość wyświetlana
)


class BookItem(models.Model):
    """
    Egzemplarz
    """
    edition = models.ForeignKey(BookEdition)
    catalog_number = models.CharField(max_length=30)
    cover_type = models.CharField(max_length=4, choices=COVER_TYPES)

    def __str__(self):
        return "{edition}, {cover}".format(edition=self.edition, cover=self.cover_type)
