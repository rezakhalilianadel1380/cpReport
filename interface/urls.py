
from django.urls import path,include
from .views import report,chart_view,generate_pdf
urlpatterns = [
    
    path('',report),
    path('chart',chart_view),
    path('pdfreport',generate_pdf),
]
