from django.db import models
from django.conf import settings

class Exercise(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    
    MUSCLE_GROUPS =[
        ('chest','Chest'),
        ('back','Back'),
        ('shoulders','Shoulders'),
        ('biceps','Biceps'),
        ('triceps','Triceps'),
        ('legs','Legs'),
    ]
    
    muscle_group = models.CharField(max_length=30,choices=MUSCLE_GROUPS)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='created_exercises'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name