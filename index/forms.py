from django import forms
from django.core.exceptions import ValidationError

from .models import *

class CreateEventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Категория не выбрана'
    class Meta:
        model = Event
        fields = ['title', 'slug', 'content', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input'}),
            'content': forms.Textarea(attrs={'class': 'form__text'}),
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 20:
            raise ValidationError('Длина превышает 20 символов')
        return title