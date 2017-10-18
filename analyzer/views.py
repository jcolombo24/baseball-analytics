from django.shortcuts import render
from urllib.parse import urlencode, parse_qs
from django.conf import settings
from django.http import HttpResponse
from .models import pitcher
from django.db.models import Q
from django.core.urlresolvers import reverse
from django_datatables_view.base_datatable_view import BaseDatatableView
import json
from analyzer.forms import PitcherFilterForm

def pitcher_view(request):
    form = PitcherFilterForm(request.GET)
    data = reverse('pitcherlist')
    
    if request.method == 'GET' and request.is_ajax():
        data = '%s' % (reverse('pitcherlist'))
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    return render(
        request,
        'analyzer/index.html',
        {'form': form, 'data': data}
    )
          
class pitcher_list_json(BaseDatatableView):
    model = pitcher
    columns = ['player_name', 'game_date','pitch_type', 'release_speed', 'pfx_x']
    order_columns = ['player_name', 'game_date','pitch_type', 'release_speed', 'pfx_x']
    
    def get_initial_queryset(self):
        return pitcher.objects.all()
    
    def filter_queryset(self, qs):
        player_name = self.request.GET.get('player_name')
        if player_name:
            qs = pitcher.objects.filter(player_name=player_name)
        return qs
    
