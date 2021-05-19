from django.db import models

# Create your models here.

class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    expression = models.CharField(max_length=100)
    submit_time = models.DateTimeField()

    client_id = models.IntegerField(default=0)
    start_time = models.DateTimeField(null=True, default=None)
    finish_time = models.DateTimeField(null=True, default=None)
    result = models.CharField(default='', max_length=100)


