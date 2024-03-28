from django.db import models
# Create your models here.
from .validations import validate_name,validate_description,validate_email,validate_username
    
class Feedback(models.Model):

    first_name = models.CharField(max_length=20, validators=[validate_name])
    last_name = models.CharField(max_length=20, validators=[validate_name])
    email = models.EmailField(validators=[validate_email])
    description=models.TextField(validators=[validate_description])
    image=models.ImageField(upload_to='feedback_images', blank=True, null=True)
   
    class Meta:
        verbose_name_plural='feedback'

    def __str__(self) -> str:
        return self.name
    
