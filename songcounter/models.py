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