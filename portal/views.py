from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cw3 import settings


# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'home.html')
