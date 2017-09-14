from django.shortcuts import render
from django.conf import settings
from django.urls import reverse
from .models import pitcher
from django_datatables_view.base_datatable_view import BaseDatatableView
import json
import operator

def pitcher_view(request):
    return render(
        request,
        'analyzer/index.html',
    )
          
class pitcherlist(BaseDatatableView):
    model = pitcher
    columns = ['player_name', 'game_date','pitch_type', 'pfx_x']
    
    def render_column(self, row, column):
        return super(pitcherlist, self).render_column(row, column)
    
    def prepare_results(self):
        json_data = [pitcher.objects.all()]
        return json_data
    
    
