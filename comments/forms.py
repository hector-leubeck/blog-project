from django.forms import ModelForm
from .models import Comments


class FormComment(ModelForm):
    def clean(self):
        data = self.cleaned_data
        name = data.get('com_name')
        comment = data.get('commentary')

        if len(name) < 2:
            self.add_error('com_name', 'Nome inválido!')
        if not comment:
            self.add_error('commentary', 'Comentário Inválido!')

    class Meta:
        model = Comments
        fields = ('com_name', 'com_email', 'commentary')
