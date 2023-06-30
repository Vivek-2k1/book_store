from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    name = models.CharField(max_length=40)
    biography = models.TextField()
    photo = models.ImageField(upload_to='store_app/image')

    def __str__(self):
        return self.name

class BookModel(models.Model):
    title = models.CharField(max_length=40)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    price = models.IntegerField()
    publication_date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='store_app/image')
    
    def __str__(self):
        return self.title

class ReviewModel(models.Model):
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    content = models.TextField()
    rating_choices = [(i,str(i)) for i in range(6)]
    rating = models.IntegerField(choices=rating_choices)