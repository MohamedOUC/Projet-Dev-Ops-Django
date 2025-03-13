from datetime import datetime
from django.shortcuts import render

# Create your views here.

def home(request):
	return render(request, "index.html", context={"date": datetime.today()})
