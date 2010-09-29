from django.db import models
from django.forms import ModelForm

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __unicode__(self):
        sb = self.first_name
        if self.middle_name != "":
            sb = sb + " " + self.middle_name

        sb = sb + " " + self.last_name

        return sb

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ManyToManyField(Author)
    rating = models.IntegerField()
    year_read = models.DateField()

    def __unicode__(self):
        sb = "title: " + self.title
        for author in self.author.all():
            sb = sb + ", author: " + str(author)
        sb = sb + ", rating: " + str(self.rating)
        sb = sb + ", year: " + str(self.year_read.year)

        return sb

class BookModelForm(ModelForm):
    class Meta:
        model = Book

class AuthorModelForm(ModelForm):
    class Meta:
        model = Author

