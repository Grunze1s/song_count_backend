from django.db import models

# Create your models here.
class Songs(models.Model):
    song_id = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=255)
    count = models.IntegerField()

    class Meta:
        db_table="counts"

    def __str__(self):
        return '{}'.format(self.song_id)

class Radio(models.Model):
    radio_id = models.IntegerField(primary_key=True)
    radio_name = models.CharField(max_length=250)
    radio_url = models.CharField(max_length=250)
    class Meta:
        db_table="radio"
    
    def __str__(self):
        return self.radio_name
    

class RadioCount(models.Model):
    radio_song_id = models.IntegerField(primary_key=True)
    radio_name = models.CharField(max_length=250)
    song_name = models.CharField(max_length=250)
    company = models.CharField(max_length=250)
    confidence = models.IntegerField()
    listened_datetime = models.DateTimeField()
    class Meta:
        ordering = ['listened_datetime']
        db_table="radio_counts"
    
    def __str__(self):
        return "{}-{}".format(self.radio_name, self.song_name)
    