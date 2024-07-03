from django.db import models
from django.contrib.auth import get_user_model

class Category(models.Model):
    name = models.CharField(max_length=100, choices=[
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
       ('Thriller', 'Thriller'),
        ('Science Fiction', 'Science Fiction'),
        ('ASction', 'Action'),
    ])

    def __str__(self):
        return self.get_name_display()
    

User = get_user_model()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    poster = models.ImageField(upload_to='posters/')
    description = models.TextField()
    release_date = models.DateField()
    actors = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    trailer_link = models.URLField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(1, '1 star'), (2, '2 stars'), (3, '3 stars'), (4, '4 stars'), (5, '5 stars')])
    comment = models.TextField()


# Create your models here.  
