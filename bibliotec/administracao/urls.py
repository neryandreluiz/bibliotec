from django.conf.urls import url, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [

    url(r'^livros/$', views.Livros.as_view()),
    url(r'^clientes/$', views.Clientes.as_view()),

    url(r'^reservas/(?P<pk>[0-9]+)/$', views.Reservas.as_view()),

    url(r'^livro_details/(?P<pk>[0-9]+)/$', views.LivroDetails.as_view()),

    url(r'^cliente_details/(?P<pk>[0-9]+)/$', views.ClienteDetails.as_view(), name='cliente_detail'),

]

urlpatterns = format_suffix_patterns(urlpatterns)

