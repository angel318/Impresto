from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
#Servicios
    url(r'^services/$', views.ServicesView.as_view()),
    url(r'^services/(?P<pk>[0-9]+)/$', views.ServicesView.as_view()),
#Tamaños de hoja
    url(r'^services/sheet-sizes/$', views.SheetSizesView.as_view()),
    url(r'^services/sheet-sizes/(?P<pk>[0-9]+)/$', views.SheetSizesView.as_view()),
#Tipos de hoja
    url(r'^services/sheet-types/$', views.SheetTypesView.as_view()),
    url(r'^services/sheet-types/(?P<pk>[0-9]+)/$', views.SheetTypesView.as_view()),
#Extras
    url(r'^services/extras/$', views.ExtrasView.as_view()),
    url(r'^services/extras/(?P<pk>[0-9]+)/$', views.ExtrasView.as_view()),
]

urlpatterns += router.urls
