from django.conf.urls import url
from placements import views


urlpatterns =[
    url(r'^$', views.index,name = 'index')

]

