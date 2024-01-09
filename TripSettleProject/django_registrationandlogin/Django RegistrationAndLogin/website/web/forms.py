

from django import forms
from .models import MyModel

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['GroupName', 'TotalMembers','Name']

    # Define widget for editable_field to use a TextInput
    GroupName = forms.CharField(widget=forms.TextInput())
    
    # Define widget for static_field to use a TextInput with the readonly attribute
    TotalMembers = forms.CharField(widget=forms.TextInput())
    
    Name = forms.CharField(widget=forms.TextInput())
