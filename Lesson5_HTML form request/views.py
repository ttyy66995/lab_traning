from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def web(request):
    try:
        name = str(request.POST.get("Name"))
        comments = str(request.POST.get("Comments"))
        number1 = int(request.POST.get("Number1"))
        number2 = int(request.POST.get("Number2"))
        number = number1 + number2
        print(name,comments,number)

        return (render(request,"my_site.html",locals()))
    except:
        return (render(request,"my_site.html",locals()))