from django.db import models


class Post(models.Model):
    """ The simple blog model. """
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    title = models.CharField(max_length=20)

    def __str__(self):
        return str(self.title)
