from django.db import models

# Create your models here.


class URLScanResult(models.Model):
    url = models.URLField()
    status = models.CharField(max_length=50)  # Safe, Malicious, Suspicious
    details = models.TextField()  # Store scan details
    scanned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} - {self.status}"
