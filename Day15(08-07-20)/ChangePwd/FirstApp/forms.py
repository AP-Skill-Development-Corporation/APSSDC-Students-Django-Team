from FirstApp.models import Change
from django.forms import ModelForm

class ChangeForm(ModelForm):
	class Meta:
		model=Change
		fields='__all__'