from django.db import models
from django.conf import settings

class Workout(models.Model):
    workout_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='workouts',null=True, blank=True
    )
    workout_date = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        try:
            return f"{self.user.user_name} - {self.workout_date}"
        except AttributeError:
            return f"Unknown User - {self.workout_date}"
    