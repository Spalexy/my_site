from django.shortcuts import render, render_to_response
from .models import Job_place
from .models import St_place

# Create your views here.
def index(request):
	name = 'Александр'
	last_name = 'Придача'
	birth = '08.11.1987'
	occupation = 'Python программист'
	phone = '+7-123-4567-88-99'
	email = 'mail@mail.com'
	site = 'pridacha.com'
	return render_to_response('index.html', {'name':name,'last_name':last_name,'birth':birth,'occupation':occupation,'phone':phone,'email':email,'site':site})


def job(request):
	job_places = Job_place.objects.all()
	return render_to_response('job.html', {'job_places':job_places})

def learn(request):
	studing_places = St_place.objects.all()
	return render_to_response('learn.html', {'studing_places':studing_places})

