import requests
from django.http import JsonResponse

def get_weather_data(request):
    if request.method == 'GET':
        location = request.GET.get('location', '')
        if not location:
            return JsonResponse({'error': 'Location parameter is missing'}, status=400)

        api_key = '4d79e55339a04667aad150429232407'
        api_url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={location}'

        try:
            response = requests.get(api_url)
            data = response.json()
            if response.status_code == 200:
                return JsonResponse(data=data)
            else:
                return JsonResponse({'error': 'Unable to fetch weather data'}, status=500)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
