from django.forms import ModelForm
from .models import Comments


class FormComment(ModelForm):
    class Meta:
        model = Comments
        fields = ('com_name', 'com_email', 'commentary')
