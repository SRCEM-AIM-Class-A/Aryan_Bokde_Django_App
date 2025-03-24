from django.shortcuts import render

# Create your views here.
def sports_page(request):
    return render(request, 'sports/sports.html')