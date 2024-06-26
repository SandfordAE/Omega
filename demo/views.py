from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
def demo(request):
    return render(request, 'demo/demo.html')



