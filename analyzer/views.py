from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from .models import pitcher
from django.urls import reverse
from django_datatables_view.base_datatable_view import BaseDatatableView
import json
from analyzer.forms import PitcherFilterForm

def pitcher_view(request):
    form = PitcherFilterForm(request.POST)
    data = reverse('pitcherlist')
    if request.method == 'POST' and request.is_ajax:
        params = request.POST.copy()
        data = ('%s?%s' % (reverse('pitcherlist'), ''.join(
            ['%s=%s&' % (k, v) for k, v in params.items()])))\
            .rstrip('&')

        return HttpResponse(json.dumps(data), content_type='application/json')
    
    return render(
        request,
        'analyzer/index.html',
        {'form': form}
    )
          
class pitcher_list_json(BaseDatatableView):
    model = pitcher
    columns = ['player_name', 'game_date','pitch_type', 'release_speed', 'pfx_x']
    order_columns = ['player_name', 'game_date','pitch_type', 'release_speed', 'pfx_x']
    
    def render_column(self, row, column):
            return super(pitcher_list_json, self).render_column(row, column)
    
    def filter_queryset(self, qs):
        search = pitcher.objects.all()
        return qs
