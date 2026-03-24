from django.db import models
import uuid

class Resume(models.Model):
    resume_id = models.CharField(max_length=20, unique=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    downloads = models.IntegerField(default=0)
    expiry_time = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.resume_id:
            self.resume_id = f"RES-{uuid.uuid4().hex[:6]}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.resume_id
class ActivityLog(models.Model):
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)