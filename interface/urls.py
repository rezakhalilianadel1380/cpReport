
from django.urls import path,include
from .views import report,chart_view
urlpatterns = [
    
    path('',report),
    path('chart',chart_view),
]
