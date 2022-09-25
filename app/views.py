from asgiref.sync import sync_to_async
from django.shortcuts import render
import asyncio
from time import sleep
import httpx
from django.http import HttpResponse

from .models import UploadSync

"""using the decorator sync_to_async This means that the synchronous function, http_call_sync, will be run in a new thread. Review the docs for more 
info. as we need interact with the db is not posible to use only library asyncIO without to use sync_to_async"""


@sync_to_async
def upload(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')

        for img in images:
            UploadSync.objects.create(images=img)
    images = UploadSync.objects.all()
    return render(request, "index.html", {'images': images})
