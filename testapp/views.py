from django.shortcuts import render

# Create your views here.
def subDomainHome(request):
    return render(request, 'sub-domain-index.html')
hello ankit