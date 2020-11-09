from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('polls/', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('delta/', views.delta, name='default'),
    path('home/', views.home, name='default'),
    path('compute/', views.compute, name='default'),
    path('storage/', views.storage, name='default'),
    path('data/', views.data, name='default'),
    path('info/', views.info, name='default'),
]