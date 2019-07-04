from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
# Create your models here.
class Player(models.Model):
    name=models.CharField(max_length=200,blank=False,default="Anon")
    player = models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    total_score=models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.name)

class Game(models.Model):
    game_id=models.CharField(max_length=200,default=None,blank=True,null=True)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    player1=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player1")
    player2=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player2")
    player3=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player3")
    player4=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player4")
    player5=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player5")


    def __str__(self):
        return str(self.game_id)

    def save(self, *args, **kwargs):
        self.game_id=get_random_string(8).lower()
        super(Game, self).save(*args, **kwargs)


class GameRound(models.Model):
    player1=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player1")
    player2=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player2")
    player3=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player3")
    player4=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player4")
    player5=models.ForeignKey(Player, on_delete=models.CASCADE,related_name="player5")
    round_number=models.IntegerField(default=0)
    game=models.ForeignKey(Game,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        i=1
        self.round_number=i
        i+=1
        
        super(PlayerRound, self).save(*args, **kwargs)