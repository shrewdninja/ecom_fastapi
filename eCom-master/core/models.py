from django.db import models
# Create your models here.
    
class Feedback(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    description=models.TextField()
    image=models.ImageField(upload_to='feedback_images', blank=True, null=True)
   
    class Meta:
        verbose_name_plural='feedback'

    def __str__(self) -> str:
        return self.name