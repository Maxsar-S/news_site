from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.tag_name


class New(models.Model):
    header = models.CharField(max_length=64)
    news_text = models.TextField(max_length=4096)
    image = models.ImageField(upload_to='news_images', blank=True)
    tags = models.ManyToManyField(Tag)
    creating_date = models.DateTimeField(auto_now_add=True)
    counter_of_viewing = models.IntegerField(default=0, editable=False)

    class Meta:
        ordering = ['-creating_date']
