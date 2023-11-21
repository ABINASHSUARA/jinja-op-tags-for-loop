from django.shortcuts import render

# Create your views here.
def forloop(request):
    d={'name':[1,2,2]}
    return render(request,'forloop.html',d)