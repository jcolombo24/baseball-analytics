from django.shortcuts import render
from .models import pitcher
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.template import RequestContext
import json
import operator
from django.http.response import HttpResponse
    
class pitcherlist(BaseDatatableView):
    model = pitcher
    columns = ['player_name', 'game_date','pitch_type', 'pfx_x']
    order_columns = ['player_name', 'game_date','pitch_type', 'pfx_x']
    max_display_length = 500
    
    def render_column(self, row, column):
        return super(pitcherlist, self).render_column(row, column)
    
    def get_initial_queryset(self):
        return pitcher.objects.all()
    