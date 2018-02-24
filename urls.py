from django.conf.urls import url
from . import views

app_name = 'ocr'

urlpatterns = [
    url(r'$', views.list, name='list'),
]
