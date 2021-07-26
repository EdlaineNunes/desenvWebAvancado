from django import forms
from django.core.mail import message
from django.core.mail.message import EmailMessage

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', max_length=100)
    emailAddress = forms.EmailField(label='Email', max_length=100)
    subjectMatter = forms.CharField(label='Assunto', max_length=100)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        emailAddress = self.cleaned_data['emailAddress']
        subjectMatter = self.cleaned_data['subjectMatter']
        message = self.cleaned_data['message']

        contents = f'Nome: {name}\nE-mail: {emailAddress}\nAssunto: {subjectMatter}\nMensagem: {message}'
        mail = EmailMessage (
            subject=subjectMatter,
            body=contents,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br', ],
            headers={'Reply.To':emailAddress},
        )
        mail.send()

