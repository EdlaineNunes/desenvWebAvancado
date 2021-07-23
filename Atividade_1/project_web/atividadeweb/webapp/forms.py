from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    emailAddress = forms.EmailField(label='Email', max_length=100)
    subjectMatter = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

