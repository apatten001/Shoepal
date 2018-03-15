from django import forms
from .models import Shoe


class CreateShoeForm(forms.ModelForm):

    class Meta:
        model = Shoe
        fields = [
            'name',
            'brand',
            'price',
            'quantity',
            ]


