from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from katas import views

urlpatterns = [
    url(r'^katas/$', views.KataList.as_view()),
    url(r'^katas/(?P<pk>[0-9]+)/$', views.KataDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)