from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    home_id = models.CharField(max_length=2000, primary_key=True)
    title = models.CharField(max_length=255)
    postnummer = models.PositiveIntegerField()
    type = models.CharField(max_length=255)
    by = models.CharField(max_length=255)
    kommune = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    energi = models.CharField(max_length=255)
    liggetid = models.PositiveIntegerField()
    areal = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    grund = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    year_built = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    year_renovated = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    pris = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    rum = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    toiletter = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    description = models.TextField()
    latitude = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    longitude = models.DecimalField(max_digits=20, decimal_places=10, default=0)
    

class Image(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='images', to_field='home_id')
    image = models.CharField(max_length=1000)
    #image = models.ImageField(upload_to='home_images')
    caption = models.CharField(max_length=255, blank=True)


class Score(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE, related_name='scores', to_field='home_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='scores')
    
    priceguess = models.DecimalField("Hvad tror du boligens udbudspris er?", max_digits=20, decimal_places=0, default=0)
    score_CHOICES = (
      (1, '1 min'),
      (2, '2'),
      (3, '3'),
      (4, '4'),
      (5, '5 max'),
    )
    score = models.PositiveIntegerField("Hvad er din vurdering af boligen?", choices=score_CHOICES, default=3)
    bidinterest_CHOICES = (
      ("Nej", 'Nej'),
      ("Ja", 'Ja'),
    )
    bidinterest = models.CharField("Ville du byde på denne bolig?", max_length=3, choices=bidinterest_CHOICES, default='Nej')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def get_difference(self):
        if (self.home.pris - self.priceguess) < 0:
          difference =  (self.home.pris - self.priceguess) * -1
        else:
          difference = (self.home.pris - self.priceguess)
        return difference
      
    def get_difference_pct(self):
        if (self.home.pris - self.priceguess) < 0.0:
          difference =  (self.home.pris - self.priceguess) * -1
        else:
          difference = (self.home.pris - self.priceguess)
        return difference / self.home.pris * 100 
      
    def get_priceguess_per_square_meters(self):
        return self.priceguess / self.home.areal
    
    def get_price_per_square_meters(self):
        return self.home.pris / self.home.areal
      
      
    
    
    

