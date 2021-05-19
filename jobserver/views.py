from django.shortcuts import render
from . import models
from datetime import datetime

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, world")

def status(request):
    text = ''
    for job in models.Job.objects.all():
        status = 'queued'
        result = ''
        if job.start_time is not None:
            status = 'running'
            if job.finish_time is not None:
                status = 'completed'
                result = ', result="job.result"'
        if job.client_id != 0:
            status += ',client={}'.format(job.client_id)

        text += 'Job {} ({}):  expression="{}{}"\n'.format(job.job_id, status, job.expression)

    return HttpResponse(text)

def submit(request, expression):
    job = models.Job.objects.create(expression=expression, submit_time=datetime.now())
    return HttpResponse("submitted expression {} as job {}".format(expression, job.job_id))

