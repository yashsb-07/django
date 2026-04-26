from django.db import models
from django.utils import timezone

# Create your models here.

class GameVarity(models.Model):
    GAME_TYPE_CHOICE = [
        ('DR', 'DRIVING'),
        ('RC', 'RACING'),
        ('PB', 'PUBG'),
        ('CH', 'CHESS'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='games/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=GAME_TYPE_CHOICE)

    def __str__(self):
        return self.name