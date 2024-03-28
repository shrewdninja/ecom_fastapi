from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from .validations import validate_email,validate_card,validate_description,validate_name,validate_username
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural='Categories'

    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    category=models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name=models.CharField(max_length=255, validators=[validate_name])
    description=models.TextField(validators=[validate_description])
    price=models.FloatField()
    image=models.ImageField(upload_to='items_images', blank=True, null=True)
    is_sold=models.BooleanField(default=False)
    created_by=models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural='items'

    def __str__(self) -> str:
        return self.name
    
class Order(models.Model):
    item = models.ForeignKey(Item, related_name = 'orders', on_delete=models.CASCADE)
    name=models.CharField(max_length=255, validators=[validate_name])
    card_info = models.CharField(max_length=16,validators=[validate_card])
    address=models.TextField(validators=[validate_description])
    
    created_by=models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name_plural='orders'

    def __str__(self) -> str:
        return self.name