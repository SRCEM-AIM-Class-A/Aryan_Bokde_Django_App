from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def academics_page(request):
    return render(request, 'academics/academics.html')