from django.shortcuts import render
from .forms import MessageForm
# Create your views here.

def acceuil(request):

    return render(request, 'html/acceuil.html')


def contact(request):
    context ={}
    
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'html/merci.html', context)

        else:
            context['errors']= form.errors.items()

    else:
        form = MessageForm()
        context['form']= form
 

    return render(request, 'html/contact.html', context)
