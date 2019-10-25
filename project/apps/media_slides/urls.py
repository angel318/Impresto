from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^slides/$', views.SlidesView.as_view()),
    url(r'^slides/(?P<pk>[0-9]+)/$', views.SlidesView.as_view()),
]

urlpatterns += router.urls
