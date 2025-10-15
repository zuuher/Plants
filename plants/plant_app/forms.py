from django import forms
from .models import user as UserModel, Plant
import re


class SignupForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput(), label="Confirm password")
    user_id = forms.CharField(required=False, label="User ID")

    class Meta:
        model = UserModel
        fields = ['name', 'email', 'phone', 'address', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if UserModel.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if not re.match(r'^\+?\d{7,15}$', phone):
            raise forms.ValidationError("Enter a valid phone number (digits, optional +).")
        return phone

    def clean(self):
        cleaned = super().clean()
        pw = cleaned.get('password')
        pw2 = cleaned.get('password_confirm')
        if pw and pw2 and pw != pw2:
            self.add_error('password_confirm', "Passwords do not match.")
        # validate optional user_id
        user_id = cleaned.get('user_id')
        if user_id:
            if not isinstance(user_id, str) or not user_id.strip():
                self.add_error('user_id', "User ID must be a non-empty string.")
        return cleaned


class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name', 'price', 'life_cycle', 'old', 'image']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or not name.strip():
            raise forms.ValidationError("Name cannot be empty.")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is None or price < 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    def clean_life_cycle(self):
        life_cycle = self.cleaned_data.get('life_cycle')
        if not life_cycle or not life_cycle.strip():
            raise forms.ValidationError("Life cycle cannot be empty.")
        return life_cycle

    def clean_old(self):
        old = self.cleaned_data.get('old')
        if old is None or old < 0:
            raise forms.ValidationError("Old must be a positive number.")
        return old

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if not image:
            raise forms.ValidationError("Image cannot be empty.")
        return image
    