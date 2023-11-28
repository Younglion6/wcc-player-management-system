from django.db import models


# Create your models here.
class Player(models.Model):
  player_number = models.PositiveIntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=100)
  role = models.CharField(max_length=50)
  subscription = models.CharField(max_length=50)

  def __str__(self):
    return f'Player: {self.first_name} {self.last_name}'
