from django.db import models
# Create your models here.
from .validations import validate_name,validate_description,validate_email,validate_username
    
class Feedback(models.Model):

    first_name = models.CharField(max_length=20, validators=[validate_name])
    last_name = models.CharField(max_length=20, validators=[validate_name])
    email = models.EmailField(max_length=50,validators=[validate_email])
    description=models.TextField(max_length=1000,validators=[validate_description])
    image=models.ImageField(upload_to='feedback_images', blank=True, null=True)
   
    class Meta:
        verbose_name_plural='feedback'

    def __str__(self) -> str:
        return self.name
    
