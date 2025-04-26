from django.shortcuts import render
from .models import Cpreport
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import os

# Create your views here.
def report(request):
    data=Cpreport.objects.raw(
        "Select TOP 300 * from  Cpreport"
    )
    context={
        "data":data

    }
    return render(request,"report.html",context)



def generate_pdf(request):
    # Assuming you have a logo file inside your static folder
    logo_path = request.build_absolute_uri('/static/logo.png')  # Update if your path is different

    html_string = render_to_string('report_template.html', {'logo_path': logo_path})

    pdf_file = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="test_report.pdf"'
    return response



def chart_view(request):
    context = {
        "labels": ["2024-01", "2024-02", "2024-03", "2024-04"],
        "pressure_data": [101, 105, 110, 108],
        "temperature_data": [23, 25, 22, 26],
        "flow_data":[15,16,10,13],
    }
    return render(request, "chart.html", context)