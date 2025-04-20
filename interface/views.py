from django.shortcuts import render
from .models import Cpreport
# Create your views here.
def report(request):
    data=Cpreport.objects.raw(
        "Select TOP 300 * from  Cpreport"
    )
    context={
        "data":data

    }
    return render(request,"report.html",context)