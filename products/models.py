from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    # owner = models.ForeignKey(User, on_delete=)
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)

    @property
    def sale_price(self):
        return f"{float(self.price) * 0.80:.2f}"

    @staticmethod
    def get_discount():
        return "122"
