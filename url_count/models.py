from django.db import models

class Url(models.Model):
    job = models.UUIDField()
    date = models.DateTimeField(auto_now_add=True)
    url_link = models.CharField(max_length=128)
    word = models.CharField(max_length=64)
    status = models.BooleanField("выполнено", default=False)
    last_update = models.DateTimeField(auto_now=True)
    result = models.CharField(max_length=64)

    #description = models.CharField(max_length=64)
    #is_completed = models.BooleanField("выполнено", default=False)

    def __str__(self):
        return self.url_link.lower()
    class Meta:
        ordering = ('-date',)
