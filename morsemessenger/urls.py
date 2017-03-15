from django.conf.urls import url
from . import views
app_name ='morsemessenger'

urlpatterns =[
    url(r'^$',views.index,name='morsemessenger'),
    url(r'^send/$', views.send,name='send'),
    url(r'^after/$', views.after,name='after'),
]
