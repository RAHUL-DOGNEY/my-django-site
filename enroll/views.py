from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def add_show(request):
    return render(request,'enroll/addshow.html')
