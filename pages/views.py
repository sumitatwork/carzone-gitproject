from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'C:/Users/Echo/Desktop/CarZone/carzone/templates/pages/home.html', {})