from django.db import models
from .user import User

class Post(models.Model):
    title_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True, blank=True) 
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    date = models.DateField()   
    
    summary = models.TextField(blank=True, default='')
    summary_generated_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.title} by {self.user.name if self.user else 'Unknown'}"