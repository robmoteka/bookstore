from django import forms
from contact.models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'message']


class ContactForm(forms.Form):
    name = forms.CharField(error_messages={'required': 'No żesz kwa... mać!'})
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea, label="Uchuchuchu",
error_messages={'required': 'No żesz kwa... mać!'})

    def clean_name(self):
        data = self.cleaned_data['name']
        if 'D' not in data:
            raise forms.ValidationError("Won! "+ data)
        return data

