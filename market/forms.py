from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Skill


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = [
            'title',
            'description',
            'category',
            'price',
            'is_free',
            'contact_preference',
            'availability_status',
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'contact_preference': forms.Select(attrs={'class': 'form-select'}),
            'availability_status': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'is_free': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        help_texts = {
            'price': 'Enter a number or leave blank if this service is free.',
        }

    def clean(self):
        cleaned_data = super().clean()
        is_free = cleaned_data.get('is_free')
        price = cleaned_data.get('price')

        if is_free:
            cleaned_data['price'] = None
        elif price is None:
            raise forms.ValidationError('Choose Free or enter a price.')

        return cleaned_data


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Use a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
