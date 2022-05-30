from django import forms
from django.forms import TextInput, Textarea, EmailInput

from .models import SendToEmail,Message


class SendToEmailForm(forms.ModelForm):
    class Meta:
        model = SendToEmail
        fields = ['mail']
        widgets = {
            'mail': EmailInput(attrs={
                'name': 'mail',
                'class': 'cform-text',
                'placeholder': 'you@your_email.com'
            })
        }


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

        widgets = {
            'name': TextInput(attrs={
                'class': 'cform-text',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': 'cform-text',
                'placeholder': 'Email'

            }),
            'company': TextInput(attrs={
                'class': 'cform-text',
                'placeholder': 'Company'
            }),
            'website': TextInput(attrs={
                'class': 'cform-text',
                'placeholder': 'Website'
            }),
            'message': Textarea(attrs={
                'class': 'cform-text',
                'placeholder': 'Message'
            })
        }

