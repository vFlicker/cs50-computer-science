from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

from yeticave.auctions.models import Listing

User = get_user_model()


class Watchlist(models.Model):
    owner: User = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="watchlist")
    item: Listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('owner', 'item')

    def __str__(self):
        return f"Watchlist for user {self.owner.username} with item {self.item.title}"