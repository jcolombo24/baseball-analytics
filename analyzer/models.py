from django.db import models

class pitcher(models.Model):

	id = models.IntegerField(primary_key=True)
	player_name = models.CharField(max_length=255, default='null')
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
	
	def __unicode__(self):
		return str(self.value)
