from django.forms import ModelForm
from basket.models import Player


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']



class EditForm(ModelForm):

	class Meta:
		model = Player
		fields = ['rut', 'dv', 'name', 'nickname', 'birthday', 'age', 'email', 'height', 'weight', 'picture', 'position', 'team']



def __init__(self):
    super(EditForm, self).__init__()
    self.fields['picture'].required = False



