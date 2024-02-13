from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length= 250)
    author = models.CharField(max_length= 250)
    description = models.TextField()

    def __str__(self) :
        return self.title
    
class Review(models.Model):
    book= models.ForeignKey(Book , on_delete=models.CASCADE)
    review_text = models.TextField()
    #rating = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
    rating = models.IntegerField(choices=[(i,i) for i in range(1 , 6)])

    def __str__(self):
        return self.book.title