import os
import random
from string import ascii_uppercase

from django.core.management.base import BaseCommand

from news.models import Tag, New
from zavod import settings


class Command(BaseCommand):
    help = 'Create data for testing'

    def add_arguments(self, parser):
        parser.add_argument('tags_count', type=int)
        parser.add_argument('news_count', type=int)

    def handle(self, *args, **options):
        Tag.objects.all().delete()
        New.objects.all().delete()
        tags_count = options['tags_count']
        news_count = options['news_count']
        tags_list = []
        image_path = settings.MEDIA_ROOT
        images = []
        for files in os.walk(image_path):
            for filename in files:
                images.append(filename)
        images = images[-1]
        for i in range(tags_count):
            tag = Tag.objects.create(tag_name=f'tag{i}')
            print(f'Tag {tag} created')
            tags_list.append(tag)
        for i in range(news_count):
            text_generator = []
            for j in range(random.randint(20, 50)):
                word_generator = ''.join(random.choice(ascii_uppercase) for i in range(random.randint(1, 10)))
                text_generator.append(word_generator)
            new = New.objects.create(header=random.choice(text_generator),
                                     news_text=" ".join(text_generator),
                                     image=f'news_images/{images[random.randint(0, len(images) - 1)]}'
                                     )
            unique_tags_list = random.sample(tags_list, random.randint(1, len(tags_list) - 1))
            for j in range(0, len(unique_tags_list)):
                new.tags.add(unique_tags_list[j - 1])
            print(f'New {new} created')
