from django.db import models

# Create your models here.
class Faculty(models.Model):
    name = models.CharField(max_length=50)
    campus = models.CharField(max_length = 10)
    
    def __str__(self):
        return self.name
        
    class Meta:
        verbose_name_plural = "faculties"