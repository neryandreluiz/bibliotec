from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^livros/$', views.Livros.as_view()),
    url(r'^livro_details/(?P<pk>[0-9]+)/$', views.LivroDetails.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

