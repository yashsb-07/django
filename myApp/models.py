from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

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
    
#One to many

class GameReview(models.Model):
    game = models.ForeignKey(GameVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.game.name}'
    
#Many to many

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    game_varieties = models.ManyToManyField(GameVarity, related_name='stores')

    def __str__(self):
        return self.name

#One to one

class GameCertificate(models.Model):
    game = models.OneToOneField(GameVarity, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.game.name}'