from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    public_date = models.DateTimeField()
    image = models.ImageField(upload_to= 'images/')
    body = models.TextField()

    def summary(self):
        return self.body[:100]  # return the first 100 characters of the content

    def pub_date(self):
        return self.public_date.strftime('%b %e %Y')  # return the publication date in a nice format

    def __str__(self):
        return self.title

