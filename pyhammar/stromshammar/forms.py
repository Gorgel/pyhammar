from django import forms
from captcha.fields import CaptchaField
from .models import WallPost
from django.forms import ModelForm, Textarea

class CaptchaWallForm(forms.ModelForm):
    my_default_errors = {
    'required': 'Du skrev in fel symboler, prova igen.',
    'invalid': 'Du skrev in fel symboler, prova igen.'
}
    captcha = CaptchaField(label=False, error_messages=my_default_errors)

    class Meta:
        model = WallPost