from django.db import models
from market.models import Items
# Create your models here.


class CartItem(models.Model):
    cart = models.ForeignKey('MyCart', null=True, blank=True)
    product = models.ForeignKey(Items)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=10.99, max_digits=1000, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        try:
            return str(self.cart.id) + " - " + self.product.item_title
        except:
            return self.product.item_title
    def __str__(self):
        try:
            return str(self.cart.id) + " - " + self.product.item_title
        except:
            return self.product.item_title


class MyCart(models.Model):
    #items = models.ManyToManyField(CartItem, null=True, blank=True)
    #products = models.ManyToManyField(Items, null=True, blank=True)
    total = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return str(self.id)

    def __str__(self):
        return "Cart-" + str(self.id)



