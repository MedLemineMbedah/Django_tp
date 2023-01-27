from django.db import models
# Create your models here.

class Book(models.Model):
    book_id=models.CharField(max_length=40)
    book_title=models.CharField(max_length=40)

    class Meta:
        app_label = 'baye_tache'

class Reviews(models.Model):
    review_id=models.CharField(max_length=40)
    review_date=models.DateField(auto_now=True)
    review_text=models.CharField(max_length=400)
    review_sentiment=models.CharField(max_length=400)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True,related_name='reviews')

