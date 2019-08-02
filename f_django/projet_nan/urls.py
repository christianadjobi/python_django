from django.urls import path

from . import views

app_name = 'projet_nan'
urlpatterns = [

    path('', views.home),
    path('match', views.match),
    path('articles', views.articles),
    path('resultat', views.date_actuelle, name='football'),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition),
    # path('scrap', views.scrap),


]