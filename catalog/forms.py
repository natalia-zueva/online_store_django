
from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'description', 'photo', 'category', 'price')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        prohibited_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in prohibited_list:
            if word in cleaned_data:
                raise forms.ValidationError("В названии продукта есть запрещенные слова")

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        prohibited_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in prohibited_list:
            if word in cleaned_data:
                raise forms.ValidationError("В описании продукта есть запрещенные слова")

        return cleaned_data