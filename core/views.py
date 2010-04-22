from core.models import *

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    stories = Story.objects.all()
    return render_to_response('core/index.html', {'stories' : stories})
