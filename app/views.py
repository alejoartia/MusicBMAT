from django.shortcuts import render

from .models import UploadSync


def upload(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')

        for img in images:
            UploadSync.objects.create(images=img)
    images = UploadSync.objects.all()
    return render(request, "index.html", {'images': images})
