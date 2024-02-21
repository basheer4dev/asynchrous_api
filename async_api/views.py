import httpx

from django.shortcuts import render
from django.http import JsonResponse

from asgiref.sync import async_to_sync
# Create your views here.

async def home(request):
    return render(request, 'index.html')


async def call_first_endpoint(request):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://quotable.io/quotes?page=1')
            response.raise_for_status()
            data = response.json()
            print(data)
    except httpx.HTTPError as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse(data, safe=False)


async def call_second_endpoint(request):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://randomuser.me/api/')
            response.raise_for_status()
            data = response.json()
            print(data)
    except httpx.HTTPError as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse(data, safe=False)