from django import forms
from .models import Register


class Registerform(forms.ModelForm):
    class Meta:
        model=Register
        fields="__all__"

    # def clean(self):
    #     email=self.cleaned_data['email']
    #     vemail=self.cleaned_data['verify_email']
    #     if email != vemail:
    #         raise forms.ValidationError("Email did not match")
