from django.shortcuts import render
import requests
from django.http import JsonResponse
# Create your views here.

def list_view(request):
    key="87b96108"
    url =f"http://www.omdbapi.com/?apikey={key}&s=avengers"
    response = requests.get(url).json()
    # response=JsonResponse(response)
    context = {
    'resps': response,
    }
    return render(request, "list.html", context)



def detail_view(request):
    key="87b96108"
    url =f"http://www.omdbapi.com/?apikey={key}&t=avengers"
    response = requests.get(url).json()
    # response=JsonResponse(response)
    context = {
    'resp': response,
    }

    return render(request, 'detail.html', context)
