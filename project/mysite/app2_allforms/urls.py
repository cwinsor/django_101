from django.urls import path

from . import views

app_name = 'app2_allforms'
urlpatterns = [
        # ex: /app2_allforms/
    path('', views.IndexView.as_view(), name='index'),
        # ex: /app2_allforms/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
