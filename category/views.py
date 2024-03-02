from django.shortcuts import render
from django.views.generic import View

from .models import Category

# Create your views here.

class HomePageView(View):
    template_name="home.html"

    def get(self, request):
        catg=Category.objects.filter(paret=None)
        context={'catg':catg}
        return render(request,template_name="home.html",context=context)
    
# def home(request):
#     catg=Category.objects.filter(paret=None)
#     context={'catg':catg}
#     return render(request,'home.html',context=context)