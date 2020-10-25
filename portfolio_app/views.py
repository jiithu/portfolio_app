from django.shortcuts import render
from .models import Works
def index(request):
    works=Works.objects
    return render(request,'portfolio_app/index.html',{'works':works})
    
# Create your views here.
