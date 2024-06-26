from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'core/index.html')


@login_required
def overview(request):
    return render(request, 'core/overview.html')

def about(request):
    return render(request, 'about/about.html')

def contact(request):
    return render(request, 'about/contact.html')

@login_required
def privacy_policy(request):
    return render(request, 'about/privacy_policy.html')

@login_required
def licensing(request):
    return render(request, 'about/licensing.html')


