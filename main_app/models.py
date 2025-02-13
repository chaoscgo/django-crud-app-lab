from django.db import models
from django.urls import reverse


OUTCOMES = (
    (True, 'I won this game!'),
    (False, 'I lost this game.')
)


class Member(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    dupr = models.FloatField()
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('member-detail', kwargs={'member_id': self.id})
    
class Game(models.Model):
    date = models.DateField('Game Date')
    winner = models.BooleanField(
        choices = OUTCOMES,
        default=OUTCOMES[False]
    )

    member = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_winner_display()} on {self.date}"