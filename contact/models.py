from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=240)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return "Message from: {name}".format(name=self.name)

