from django.urls import path
from django.views.generic import TemplateView

#from . import views
from app2_allforms.views import WhateverView
from app2_allforms.views import NeverlandView
from app2_allforms.views import IndexView
from app2_allforms.views import DetailViewA
from app2_allforms.views import DetailViewB
from app2_allforms.views import DetailViewC
from app2_allforms.views import EverythingCreate
from app2_allforms.views import EverythingDetail
from app2_allforms.views import EverythingUpdate
from app2_allforms.views import EverythingDelete



from . import views
from .models import ModelAllFormTypes

app_name = 'app2_allforms'
urlpatterns = [

    # as explained in:
    # https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/
    # there are a variety of views.

    # this uses the generic.TemplateView - no need to make a derived view class
    path('whomever/', TemplateView.as_view(template_name="app2_allforms/whomever.html")),

    # this uses a view derived from View 
    path('whatever/', WhateverView.as_view(), name='whatever'),

    # this uses a view derived from TemplateView
    path('neverland/', NeverlandView.as_view()),

    # for the index (list) we subclass ListView
    path('', views.IndexView.as_view()),

    # for the detail.. subclass DetailView and provide implementation of get_context_data
    # ex: /app2_allforms/A/5/
    path('A/<int:pk>/', DetailViewA.as_view(), name='detailA'),

    # The default implementation adds the object being displayed to the template, but you
    # can override it to send more:
    path('B/<int:pk>/', DetailViewB.as_view(), name='detailB'),

    # as described at
    # https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-editing/
    # can generate forms class
    path('C/<int:pk>/', DetailViewC.as_view(), name='detailC'),


    path('everything/add/', EverythingCreate.as_view(), name='everything-add'),
    path('everything/<int:pk>/detail/', EverythingDetail.as_view(), name='everything-detail'),
    path('everything/<int:pk>/update/', EverythingUpdate.as_view(), name='everything-update'),
    path('everything/<int:pk>/delete/', EverythingDelete.as_view(), name='everything-delete'),
]

