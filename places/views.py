import json

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

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
                'coordinates': [place.longitude, place.latitude]
            },
            'properties': {
                'title': place.title,
                'placeId': place.id,
                'detailsUrl': reverse('display_place', kwargs={'place_id': place.id})
            }
        }
        places['features'].append(place_layout)

    context = {
        'places': json.dumps(places)
    }

    return render(request, 'index.html', context)


def display_place(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related("pictures"),
        id=place_id
    )

    response = {
        'title': place.title,
        'imgs': [image.image.url for image in place.pictures.all()],
        'description_short': place.short_description,
        'description_long': place.long_description,
        'coordinates': {
            'lat': place.latitude,
            'lng': place.longitude
        }
    }

    return JsonResponse(response, json_dumps_params={'indent': 2, 'ensure_ascii': False})
