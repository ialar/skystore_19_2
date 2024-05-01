from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordResetForm

from catalog.forms import StyleFormMixin
from users.models import User


class LoginCustomForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class RegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserPasswordResetForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)
