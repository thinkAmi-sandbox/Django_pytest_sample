from django import forms
from django.core.exceptions import ValidationError
from .models import Item


def validate_alphabet_only(value):
    if value.isalpha() == False:
        raise ValidationError(
            ('form_onlyの値 {} にアルファベット以外が含まれています'.format(value)),
            params={'value': value},
        )


class ItemModelForm(forms.ModelForm):
    form_only = forms.CharField(validators=[validate_alphabet_only])

    class Meta:
        model = Item
        fields = '__all__'