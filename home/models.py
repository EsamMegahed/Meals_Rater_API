from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.


class Meal(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length =500)

    def no_of_ratings(self):
        ratings = Rating.objects.filter(meal=self)
        return len(ratings)
    
    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(meal=self)
        for rate in ratings:
            sum += rate.stars
        if len(ratings) > 0:

            return sum / len(ratings)
        else:
            return 0

    def __str__(self) -> str:
        return self.title
    
class Rating(models.Model):
    meal = models.ForeignKey(Meal,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    def __str__(self) -> str:
        return str(f"Meal : {self.meal}   |  User = {self.user}")
    
    class Meta:
        unique_together = (('user','meal'),)
        index_together = (('user','meal'),)