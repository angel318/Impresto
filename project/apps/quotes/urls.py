from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
#Servicios
    url(r'^quotes/$', views.QuotesView.as_view()),
    url(r'^quotes/(?P<pk>[0-9]+)/$', views.QuotesView.as_view()),

]

urlpatterns += router.urls
