import json

from django.shortcuts import render
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