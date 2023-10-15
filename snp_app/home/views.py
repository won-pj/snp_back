from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    message = request.GET.get('abc')
    print(message)

    return HttpResponse("안녕 - 파이썬이 보내는 메시지")