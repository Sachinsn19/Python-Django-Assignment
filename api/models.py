from datetime import timezone
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Products(models.Model):
    TYPES = (
        ('fashion', _("Fashion")),
        ('mobiles', _("Mobiles")),
        ('home', _("Home")),
        ('appliances',_("Appliances")),
        ('grocery', _("Grocery")),
        ('personal_care', _("Personal Care")),
        ('sports', _("Sports")),
        ('electronics', _("Electronics")),
        ('toys_baby', _("Toys & Baby")),
    )
    name = models.CharField(max_length=255, verbose_name=_("Product Name"))
    category = models.CharField(max_length=255,choices=TYPES, default=0, verbose_name=_("Products Category"))
    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name=_("Product Cost"))
    discount = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Discount Price"))
    created = models.DateTimeField(auto_now_add=True, verbose_name=_("Product Created"))
    is_active = models.BooleanField(default=True, verbose_name=_("Active Status"))
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE, blank=True,null=True)

    def __str__(self):
        return self. name
    class Meta:
        ordering = ['created']

    