from django.shortcuts import render
from django.template import loader
from polls.models import Filial
from django.core import serializers
from polls.forms import Coordinate

# Create your views here.
def index(request):
    filials = Filial.objects.all()
    context = {
        'filials': serializers.serialize("json", filials)
    }
    return render(request, 'index.html', context=context)

def saveCoord(request):
    if request.method == 'POST':
        form = Coordinate(request.POST)
        if form.is_valid():
            filial = Filial.objects.get(pk=form.cleaned_data['code'])
            filial.geocode = form.cleaned_data['geocode']
            filial.save()