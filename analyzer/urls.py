from django.conf.urls import url
from analyzer import views
from django.conf.urls.static import static, settings
from analyzer.views import pitcherlist, pitcher_view
from django.urls import reverse
import json


urlpatterns = [
    url(r'^$', views.pitcher_view, name='pitcherview'),
    url(r'^$', pitcherlist.as_view(), name='pitcherlist'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
