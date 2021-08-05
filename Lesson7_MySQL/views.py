from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,JsonResponse
from stock_search.models import StockName   

def web(request):
    return (render(request,"stock_search.html"))

@csrf_exempt
def Ajax_func(request):
    code_input = request.POST.get('code_input')                                #使用者輸入的股票代碼
    stock_name = StockName.objects.get(code=code_input).stock 

    return JsonResponse({'stock_name':stock_name})     #丟回去前端