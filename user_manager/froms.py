from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):

    def v(self):
        # if(self[0] != 'a'):
        #    raise ValidationError("name should start with a")
        pass

    username = forms.CharField(validators=[v])
    password = forms.CharField(validators=[v])
