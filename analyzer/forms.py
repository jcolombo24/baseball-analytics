from django import forms
from .models import pitcher

class pitcherform(forms.ModelForm):
    class Meta:
        model = pitcher
        fields = ('player_name')

    def __init__(self, user, *args, **kwargs):
        super(pitcherform, self).__init__(*args, **kwargs)
        self.fields['player_name'].queryset = Category.objects.all