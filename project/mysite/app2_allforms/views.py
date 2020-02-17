from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.urls import reverse_lazy

from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from .models import ModelAllFormTypes
from .forms import MyFormC


class WhateverView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('You have reached the Whatever page!')


class NeverlandView(TemplateView):

    template_name = 'app2_allforms/neverland.html'


class IndexView(ListView):

    model = ModelAllFormTypes
    template_name = 'app2_allforms/index.html'
    context_object_name = 'the_context_object'


class DetailViewA(DetailView):

    model = ModelAllFormTypes
    template_name = 'app2_allforms/detailA.html'
    context_object_name = 'the_context_object'


class DetailViewB(DetailView):

    model = ModelAllFormTypes
    template_name = 'app2_allforms/detailB.html'
    context_object_name = 'the_context_object'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['book_list'] = Book.objects.all()
        context['message'] = "this is a message"
        return context


class DetailViewC(FormView):
    template_name = 'app2_allforms/detailC.html'
    form_class = MyFormC
    success_url = '/neverland/'
    context_object_name = 'the_context_object'

    def form_valid(self,form):
        return super().form_valid(form)


class EverythingDetail(DetailView):
    model = ModelAllFormTypes
    template_name = 'app2_allforms/everything_detail.html'
    fields = 'your_name'


class EverythingCreate(CreateView):
    model = ModelAllFormTypes
    template_name = 'app2_allforms/everything_add.html'
    fields = 'your_name'


class EverythingUpdate(UpdateView):
    model = ModelAllFormTypes
    template_name = 'app2_allforms/everything_update.html'
    fields = 'your_name'


class EverythingDelete(DeleteView):
    model = ModelAllFormTypes
    template_name = 'app2_allforms/everything_delete.html'
    success_url = reverse_lazy('app2_allforms')


#   def do_view_b(self, request):
#       # if this is a POST request we need to process the form data
#       if request.method == 'POST':
#           # create a form instance and populate it with data from the request:
#           form = AllTypesFormB(request.POST)
#           # check whether it's valid: 
# 
#           if form.is_valid():
#               # process the data in form.cleaned_data as required
#               # ...
#               # redirect to a new URL:
#               return HttpResponseRedirect('/thanks/')
#
#        # if a GET (or any other method) we'll create a blank form
#        else:
#            form = AllTypesFormB()
#
#        return render(request, 'name.html', {'form': form})

#def do_view_b(request, the_pk):
#    modelAllFormTypes = get_object_or_404(ModelAllFormTypes, pk=the_pk)

#    # if this is a POST request we need to process the form data
#    if request.method == 'POST':
#        # create a form instance and populate it with data from the request:
#       form = AllTypesFormB(request.POST)
#       # check whether it's valid:
#       #if form.is_valid():
#            # process the data in form.cleaned_data as required
#            # ...
#            # redirect to a new URL:
#            #return HttpResponseRedirect('/thanks/')

#    # if a GET (or any other method) we'll show the form data
#   else:
#        #data = {
#        #    'the_name': 'hello'}
#        #form = AllTypesFormB(data)

#        form = AllTypesFormB(modelAllFormTypes.get_fields())

#        #form = AllTypesFormB({'alpha':'the_alpha', 'beta':'the_beta'})
#        #form.your_name = "hello123"
#        #return HttpResponseRedirect('/thanks/')
#        #return HttpResponseRedirect('/app2_allforms/')
#        #return render(request, 'app2_allforms/B/3', {'form': form})
#        #return render(request, 'name.html', {'form': form})
#        return render(request=request, template_name='app2_allforms/detailB.html', context={'form': form})
