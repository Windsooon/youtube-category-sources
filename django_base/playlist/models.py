from django.db import models
from inner.models import Inner


class Playlist(models.Model):
    inner = models.ForeignKey(
        Inner, related_name="playlist", on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    real_id = models.CharField(max_length=50)
    channel_id = models.CharField(max_length=50)
    channel_title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    thumbnails = models.URLField()
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(blank=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " / " + self.channel_title
