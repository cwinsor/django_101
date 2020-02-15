from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.views import generic

from .models import ModelAllFormTypes


class IndexView(generic.ListView):
    template_name = 'app2_allforms/index.html'
    context_object_name = 'the_context_object'

    def get_queryset(self):
        return ModelAllFormTypes.objects.all()

class DetailView(generic.DetailView):
    template_name = 'app2_allforms/detail.html'
    model = ModelAllFormTypes
    context_object_name = 'the_context_object2'
