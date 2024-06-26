from django import forms
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'

            # if field_name != 'is_active':
            #     field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin):
    FORBIDDEN_TERMS = [
        'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'
    ]

    class Meta:
        model = Product
        exclude = ('count_of_views', 'owner')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in self.FORBIDDEN_TERMS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Недопустимое слово "{word.upper()}" в названии продукта')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in self.FORBIDDEN_TERMS:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Недопустимое слово "{word.upper()}" в описании продукта')
        return cleaned_data


class ProductModeratorForm(StyleFormMixin):
    class Meta:
        model = Product
        fields = ('category', 'description', 'is_published')


class VersionForm(StyleFormMixin):
    class Meta:
        model = Version
        fields = '__all__'
