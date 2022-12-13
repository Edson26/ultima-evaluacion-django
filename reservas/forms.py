from django.forms import forms
from .models import Inscritos, Instituto

class FormInscritos(forms.ModelForm):
    class Meta:
        model = Inscritos
        fields = '__all__'
        
class FormInstituto(forms.ModelForm):
    class Meta:
        model = Instituto
        fields = '__all__'