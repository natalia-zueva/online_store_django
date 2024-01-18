
from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ('owner', 'create_data', 'last_change_data',)

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


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


class ModeratorForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published',)
