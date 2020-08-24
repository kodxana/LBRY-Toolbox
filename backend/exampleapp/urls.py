from django.urls import path
from django.conf.urls import include, url

from . import views

app_name = 'exampleapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('step1', views.Step1_View, name='step1'),
    
]
