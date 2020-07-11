from FirstApp.models import Movies
from django.forms import ModelForm
class MoviesForm(ModelForm):
	class Meta:
		model=Movies
		fields='__all__'