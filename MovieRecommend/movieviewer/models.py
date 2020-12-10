from django.db import models


# Create your models here.
class Movie(models.Model):
    tconst = models.CharField(max_length=30, primary_key=True)
    titleType = models.CharField(max_length=550, blank=True, null=True)
    primaryTitle = models.CharField(max_length=550, blank=True, null=True)
    originalTitle = models.CharField(max_length=550, blank=True, null=True)
    startYear = models.CharField(max_length=550, blank=True, null=True)
    runtimeMinutes = models.CharField(max_length=550, blank=True, null=True)
    genres = models.CharField(max_length=550, blank=True, null=True)


class Rating(models.Model):
    tconst = models.OneToOneField(
        Movie, on_delete=models.CASCADE, primary_key=True,)
    averageRating = models.CharField(max_length=550, blank=True, null=True)
    numVotes = models.CharField(max_length=550, blank=True, null=True)

