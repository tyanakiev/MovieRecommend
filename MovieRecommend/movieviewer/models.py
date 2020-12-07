from django.db import models


# Create your models here.
class Movie(models.Model):
    imdb_title_id = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=550)
    original_title = models.CharField(max_length=550, blank=True, null=True)
    year = models.CharField(max_length=30, blank=True, null=True)
    date_published = models.CharField(max_length=250, blank=True, null=True)
    genre = models.CharField(max_length=250, blank=True, null=True)
    duration = models.CharField(max_length=30, blank=True, null=True)
    country = models.CharField(max_length=350, blank=True, null=True)
    language = models.CharField(max_length=350, blank=True, null=True)
    director = models.CharField(max_length=350, blank=True, null=True)
    writer = models.CharField(max_length=450, blank=True, null=True)
    production_company = models.CharField(max_length=450, blank=True, null=True)
    actors = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    avg_vote = models.CharField(max_length=30, blank=True, null=True)
    votes = models.CharField(max_length=30, blank=True, null=True)
    budget = models.CharField(max_length=20, blank=True, null=True)
    usa_gross_income = models.CharField(max_length=30, blank=True, null=True)
    worlwide_gross_income = models.CharField(max_length=30, blank=True, null=True)
    metascore = models.CharField(max_length=30, blank=True, null=True)
    reviews_from_users = models.CharField(max_length=30, blank=True, null=True)
    reviews_from_critics = models.CharField(max_length=30, blank=True, null=True)
