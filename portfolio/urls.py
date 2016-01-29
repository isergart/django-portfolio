from django.conf.urls import url
from . import views

app_name = 'portfilio'

urlpatterns = [
    url(r'^$', views.current_date),
    # url(r'^$', views.index, name='index'),
    url(r'^time/plus/(\d{1,2})/$', views.hours_ahead),
]
