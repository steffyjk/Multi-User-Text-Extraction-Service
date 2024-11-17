from django.db import models

class DocumentDetails(models.Model):
    file = models.FileField(upload_to='documents/')
    url = models.URLField(blank=True, null=True)
    extracted_text = models.TextField(blank=True, null=True)
    email = models.EmailField()
    status = models.CharField(max_length=20, default='PENDING')  # PENDING, PROCESSING, COMPLETED
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
