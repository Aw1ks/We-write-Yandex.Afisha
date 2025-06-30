import json

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from places.models import Place


def index(request):
    places = {
        'type': 'FeatureCollection',
        'features': []
    }

    for place in Place.objects.all():
        place_layout = {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': [place.latitude, place.longitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': '../static/places/moscow_legends.json' # Тестовые данные
            }
        }
        places['features'].append(place_layout)

    context = {
        'places_json': json.dumps(places)
    }

    return render(request, 'index.html', context)


def see_place_by_id(request, place_id):
    place = get_object_or_404(Place, id=place_id)

    urthjo9gbh = {
        'title': place.title,
        'imgs': [image.image.url for image in place.pictures.all()],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }

    return JsonResponse(urthjo9gbh, json_dumps_params={'indent': 2, 'ensure_ascii': False})
