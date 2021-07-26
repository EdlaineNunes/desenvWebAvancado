from django.shortcuts import render
from .forms import * 
from django.contrib import messages

# Create your views here.


def index(request):
    # context = {
    #     'curso': 'Sistemas de Informação'
    # }
    # return render(request, 'index.html', context)
    return render(request, 'index.html')


def w3c(request):
    return render(request, 'w3c.html')


def html(request):
    return render(request, 'html.html')


def css(request):
    return render(request, 'css.html')


def javascript(request):
    return render(request, 'javascript.html')


def frontend(request):
    return render(request, 'frontend.html')


def backend(request):
    return render(request, 'backend.html')

def contact(request):
    form = ContactForm(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso')
            form = ContactForm()

        else:
            messages.error(request,'Erro ao enviar e-mail')

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

