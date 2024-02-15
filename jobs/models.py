import datetime
from datetime import timedelta
from django.db import models
from django.utils import timezone
from django.utils.timezone import now

class BaseModel(models.Model):
    objects = models.Manager()
    DoesNotExist = models.Manager()

    class Meta:
        abstract = True

class Job(BaseModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    company = models.CharField(max_length=100, default='')
    pub_date = models.DateTimeField(default=timezone.now)
    expiration_date = models.DateTimeField(default=now() + timedelta(days=30))

    def __str__(self):
        return self.title

    def is_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=7)

class Application(BaseModel):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant_name = models.CharField(max_length=100)
    applicant_email = models.EmailField()
    resume = models.TextField()

    def __str__(self):
        return f"Application for {self.job.title} by {self.applicant_name}"