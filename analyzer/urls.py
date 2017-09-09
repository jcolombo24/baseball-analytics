from django.conf.urls import url
from analyzer import views
from analyzer.views import pitcherlist
import json

urlpatterns = [
    url(r'^$', pitcherlist.as_view(), name='pitcherlist'),
]
