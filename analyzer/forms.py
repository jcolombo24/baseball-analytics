from datetime import date, timedelta
import itertools
from django import forms
import operator
from .models import pitcher
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import FormActions
from crispy_forms.layout import Layout, Button, Submit, MultiField, Div, HTML, \
    Field, Fieldset, Reset

DATE_FORMAT = '%m/%d/%Y'

class PitcherFilterForm(forms.Form):
    player_name = forms.ModelChoiceField(
        queryset=pitcher.objects.order_by('player_name').values_list('player_name', flat=True).distinct(), required=True)
    
    def __init__(self, *args, **kwargs):
        super(PitcherFilterForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'filter_form'
        self.helper.form_method = 'post'
        self.helper.form_action = '.'
        self.helper.layout = Layout(
            Field('player_name'),
            FormActions(
                Submit('submit', 'Filter'),
                Reset('reset', 'Reset'),),
                )
                           
