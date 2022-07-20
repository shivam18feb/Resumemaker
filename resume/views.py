from django.shortcuts import render
from .forms import resumedata

# Create your views here.
def resume(request):
	return render(request,'index.html')


def resume1(request):
	return render(request,'fresher.html')


def resume2(request):
	return render(request,'exp.html')

def resume3(request):
	return render(request,'temp.html')

def resume4(request):
	return render(request,'about.html')

def resume5(request):
	return render(request,'signup.html')


def showfromdata(request):
	fm=resumedata()
	return render(request,'data.html',{ 'form':fm })