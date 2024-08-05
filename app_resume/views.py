from datetime import datetime
from django.shortcuts import render

def index(request):
    context = {}
    context['today'] = datetime.today()
    return render(request, 'index.html', context)