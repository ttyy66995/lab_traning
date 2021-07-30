from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def web(request):
    return (render(request,"test_ajax.html"))


@csrf_exempt
def Ajax_func(request):
    
    name = request.POST.get('name')
    comments = request.POST.get('comments')
    number1 = request.POST.get('number1')
    number2 = request.POST.get('number2')
    print(name,comments,number1,number2)

    number = int(number1) + int(number2)

    return JsonResponse({'result_name':name,'result_comments':comments,'result_number':number})
