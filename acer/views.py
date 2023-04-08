from django.shortcuts import render

# Create your views here.
def Show_view(request):
    return render(request,"index.html")

def Add(request):
    return render(request,"about.html")