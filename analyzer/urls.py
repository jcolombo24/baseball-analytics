from django.conf.urls import url
from analyzer import views
from django.conf.urls.static import static, settings
from analyzer.views import pitcher_list_json, pitcher_view

urlpatterns = [
    url(r'^$', views.pitcher_view),
    url(r'^analyzer/$', pitcher_list_json.as_view(), name='pitcherlist'),
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
