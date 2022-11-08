from django.forms import ModelForm

from facts.models import Fact


class FactForm(ModelForm):
    class Meta:
        model = Fact
        fields = ['fact']
