import json
import requests

from django.core.management.base import BaseCommand, CommandError
from django.core.files.base import ContentFile

from places.models import Pictures_places, Place


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '-u',
            '--url',
            action='store',
            help='Import JSON data by link'
        )

        parser.add_argument(
            '-p',
            '--path',
            action='store',
            help='Import JSON data from a local file'
        )

    def handle(self, *args, **options):
        if options['url']:
            fetch_and_load_place(options['url'], url=True)
        if options['path']:
            fetch_and_load_place(options['path'])


def fetch_and_load_place(json_path: str, url=False):
    if url:
        try:
            response = requests.get(json_path)
            response.raise_for_status()
            imported_place = response.json()
            return load_place_info(imported_place)

        except (requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError):
            raise CommandError('Error fetching data or invalid JSON received from URL')

    else: 
        try:
            with open(json_path, 'r', encoding='utf-8') as file:
                places_json_urls =  json.load(file)
                return load_place_info(places_json_urls)

        except (FileNotFoundError, UnicodeDecodeError):
            raise CommandError(f'File not found: {json_path} or invalid JSON received')


def load_place_info(json_info):
    try:
        place, created = Place.objects.get_or_create(
            title=json_info['title'],
            latitude=float(json_info['coordinates']['lat']),
            longitude=float(json_info['coordinates']['lng']),
            defaults={
                'description_long': json_info.get('description_long', ''),
                'description_short': json_info.get('description_short', ''),
            }
        )
    except MultipleObjectsReturned:
        raise CommandError(f'Multiple places found with title {json_info["title"]} and given coordinates.')

    if not created:
        raise CommandError(f'Location already exists: {json_info["title"]}')

    for index, image_url in enumerate(json_info['imgs'], start=1):
        image_name = f'{json_info['title']}_{index}.jpg'
        try:
            download_and_save_image(place, image_url, image_name, index)

        except:
            raise CommandError(f'Failed to load image. Number: {index}, Location: {json_info['title']}')


def download_and_save_image(place, image_url, image_name, index):
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    Pictures_places.objects.create(
        place=place,
        order=index,
        image=ContentFile(
            image_response.content,
            name=image_name
        )
    )