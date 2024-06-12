from django.db import models

# Create your models here.


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Author(TimeStamp):
    name = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author')
    profession = models.CharField(max_length=212)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(TimeStamp):
    name = models.CharField(max_length=212)

    def __str__(self):
        return self.name


class Article(TimeStamp):
    title = models.CharField(max_length=212)
    image = models.ImageField(upload_to='author')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class Comment(TimeStamp):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=212)
    email = models.EmailField()
    website = models.URLField()
    message = models.TextField()

    def __str__(self):
        return self.name


class About(TimeStamp):
    title = models.CharField(max_length=212)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.title



