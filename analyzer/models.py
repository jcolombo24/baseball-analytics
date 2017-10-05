from django.db import models

class pitcher_manager(models.Manager):
    
    def by_player(self, player_name,):
        return self.distinct()
    
    def by_date(self, start_date, end_date, **kwargs):
        resultset = self.filter(
            game_date__gte=start_date,
            game_date__lte=end_date,
        )
        return resultset.order_by('-game_date')

class pitcher(models.Model):
    objects = pitcher_manager()

    player_name = models.CharField('names', max_length=255, default='null')       
    pitch_type = models.CharField(max_length=255, default='null')
    game_date = models.DateField(null=True, blank=True)
    release_speed = models.FloatField()
    pfx_x = models.FloatField()
    pfx_z = models.FloatField()
    spin_rate = models.FloatField()
    estimated_ba_using_speedangle = models.FloatField()
    estimated_woba_using_speedangle = models.FloatField()
    babip_value = models.FloatField()
    Usage = models.FloatField()
    id = models.IntegerField(primary_key=True)
    
    def __unicode__(self):
        return str(self.player_name)
