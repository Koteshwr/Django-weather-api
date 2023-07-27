# Django Weather API

This repository contains a Django API that fetches weather data from the WeatherAPI and generates a JSON response. The API is designed to handle Cross-Origin Resource Sharing (CORS) using the django-cors-headers package, allowing it to be used by frontend applications from different origins. The API is successfully hosted on AWS.
Features

   1. Fetch weather data from the WeatherAPI.
   2. Generate JSON response containing weather details.
   3. Handle CORS to enable cross-origin requests.

## Prerequisites

Before running the Django Weather API, ensure that you have the following installed:

   1.Python (v3.6 or above)
   2.Django (v3.x or above)
   3.django-cors-headers package

## Getting Started

Follow these steps to set up and run the Django Weather API:

   Clone the repository:

```python
git clone https://github.com/your-username/django-weather-api.git
cd django-weather-api
```
    
   Install the required Python packages (preferably in a virtual environment):

```python

pip install -r requirements.txt
```
   Configure Django CORS Headers:

   Open the settings.py file in your Django project.

   Add 'corsheaders' to the INSTALLED_APPS list:
        
```python
INSTALLED_APPS = [
    # Other installed apps...
    'corsheaders',
]
```
   Add the CorsMiddleware to the MIDDLEWARE list (should be placed as high as possible):
    

```python

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    # Other middleware...
]
```
    
   Configure CORS settings:
    

```python

    # Allow requests from all origins (for development purposes)
    CORS_ALLOW_ALL_ORIGINS = True
```
    
   Note: In a production environment, it is recommended to specify specific origins rather than allowing all origins.

   Run the Django development server:

```python
python manage.py runserver
```

The Django Weather API should now be running at http://localhost:8000.

## API Endpoints

The Django Weather API provides the following endpoint:

   GET /weather/?city=<city-name>: Fetch weather data for the specified <city-name> from the WeatherAPI and generate a JSON response containing weather details.

## Contributing

If you'd like to contribute to this project, feel free to submit pull requests or open issues in the repository. Your contributions are welcome!
## License

This project is licensed under the MIT License - see the LICENSE file for details.
## Acknowledgments

   Thanks to the WeatherAPI for providing weather data for this project.
   
   Thanks to the Django and Python communities for their valuable resources and support.
