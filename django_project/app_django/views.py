from django.http import HttpResponse

# Create your views here.

def home(request):
	return HttpResponse("Projet DevOps en cours de création")
