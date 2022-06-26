from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(
        max_length=50, blank=False, primary_key=True, unique=True
    )
    creation_date = models.DateTimeField(auto_now_add=True)
    reading_goal = models.IntegerField(blank=False)


class Book(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=200)
    pages = models.IntegerField(blank=False)

    def __str__(self):
        return self.title,\
               self.author, \
               f"{self.pages} pages"


class Update(models.Model):
    BOOK_FINISHED = [("Y", "YES"), ("N", "NO")]
    date = models.DateTimeField(auto_now_add=True)
    pages_read = models.IntegerField(blank=False)
    progress = models.CharField(max_length=3, choices=BOOK_FINISHED, default="N")

    def pages_left(self):
        pages = Book.pages - self.pages_read
        return f"You have {pages} pages left to read."
