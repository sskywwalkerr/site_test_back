from django.shortcuts import render
from .models import Artiсles
def news_home(request):
    news = Artiсles.objects.all()
    return render(request, 'news/news_home.html')
