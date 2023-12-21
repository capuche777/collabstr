import json

from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import JsonFile
from creators.models import Creator, Content


@receiver(post_save, sender=JsonFile)
def create_json_file(sender, instance, created, **kwargs):
    """
    After upload the json file, it will populate the db to their corresponding model
    """
    if created:
       with open(f'media/{instance}') as json_file:
            data = json.load(json_file)

            for i, k in enumerate(data):
                # It is not able to separate firstname and lastname, it will be saved on firstname
                _platform = k['platform'].lower()  # cast to lower because of the PLATFORM_CHOICES FIELD

                user, created = User.objects.get_or_create(first_name=k['name'], username=k['username'])
                creator, created = Creator.objects.get_or_create(user=user, rating=k['rating'], platform=_platform)
                content, created = Content.objects.get_or_create(user=user, url=k['content'])
