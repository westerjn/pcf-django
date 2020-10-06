# -*- coding: utf-8 -*-
from django.urls import path
from . import views
from warapp import urls

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('war/', views.warindex, name='warindex'),
    path('six/', views.pageSix, name='game'),
]
