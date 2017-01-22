from django import forms
from .models import Message
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        widgets = {'text': forms.TextInput(attrs={'placeholder': 'Write your message here...'})}
        fields = ["text"]


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ["username"]
