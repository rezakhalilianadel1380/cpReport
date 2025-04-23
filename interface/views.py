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




def chart_view(request):
    context = {
        "labels": ["2024-01", "2024-02", "2024-03", "2024-04"],
        "pressure_data": [101, 105, 110, 108],
        "temperature_data": [23, 25, 22, 26],
    }
    return render(request, "chart.html", context)