from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from shelf.models import BookItem



class Rental(models.Model):
    who = models.ForeignKey(User)
    what = models.ForeignKey(BookItem)
    when = models.DateTimeField(default=now)
    returned = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{book} {user} {rent} {ret}'.format(book=self.what, user=self.who, rent=self.when, ret=self.returned)