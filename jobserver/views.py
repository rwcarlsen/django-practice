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

        text += 'Job {} ({}):  expression="{}{}" <br>'.format(job.job_id, status, job.expression, result)

    return HttpResponse(text)

def timed_recipes(signal):
    for r in models.Recipe.objects.all():
        cron_ready_to_run(r.cron_text, datetime.now())



def report(request, job_id, result):
    j = models.Job.objects.get(job_id=job_id)
    j.result = result
    j.finish_time = datetime.now()
    j.save()
    return HttpResponse('job {} result successfully recorded'.format(job_id))

def fetch(request, client_id):
    jobs = models.Job.objects.filter(start_time__isnull=True)
    if len(jobs) == 0:
        return HttpResponse('no jobs')

    j = jobs[0]
    j.client_id = client_id
    j.start_time = datetime.now()
    j.save()

    return HttpResponse('job {}\t{}'.format(j.job_id, j.expression))


def submit(request, expression):
    job = models.Job.objects.create(expression=expression, submit_time=datetime.now())
    return HttpResponse("submitted expression {} as job {}".format(expression, job.job_id))

