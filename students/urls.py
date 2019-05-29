from django.conf.urls import url
from .views import *
from students import views
app_name = 'students'

urlpatterns= [
	url(r'^$',views.RetrieveAll,name='RetrieveAll'),
    url(r'^student/Create/$', views.CreateStudent, name = 'CreateStudent'),
    url(r'^student/detail/(?P<pk>\d+)$',views.Retrieve,name='detail'),
    url(r'^student/delete/(?P<pk>\d+)$',views.delete,name='delete'),
    url(r'^student/update/(?P<pk>\d+)$',views.update,name='update'),

]
