from django.db import models

from .utils import create_shortened_url

# Create your models here.

class Shortener(models.Model):
    
    created = models.DateField(auto_now_add=True)
    
    times_followed = models.PositiveIntegerField(default=0)
    
    long_url = models.URLField()
    
    short_url = models.URLField(max_length=15, unique=True, blank=True)
    
    class Meta:
        
        ordering = ['-created']
        
    def __str__(self) -> str:
        
        return f'{self.long_url} to {self.short_url}'
    
    def save(self, *args, **kwargs):
        
        if not self.short_url:
            self.short_url = create_shortened_url(self)
            
        super().save(*args, **kwargs)
        
    
