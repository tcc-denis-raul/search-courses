from django.conf.urls import url

from . import views

app_name = 'search'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^task$',views.TaskCallView.as_view(), name='task'),
    url(r'^blacklist/(?P<url>.*)/(?P<name>.*)$', views.BlackListView.as_view(), name='black'),
]
