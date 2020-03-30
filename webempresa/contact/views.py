from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.

def contact (request):
    contact_form =ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Envámos el correo, redireccionamos
            email = EmailMessage(
                    #asunto
                        "La Caffetiera: Nuevo mensaje de contacto",
                    #Cuerpo
                        "De {} <{}>\n\nEscribió\n\n{}".format(name, email, content),
                    #email_origen
                        "no-contestar@inbox.mailtrap.io",
                    #email_destino
                        ["adonislozada@gmail.com"],
                    #Reply_to
                    reply_to=[email]
            )
        try:
            email.send()
            #Todo ha salido bien, redireccionamos a OK
            return redirect(reverse('contact')+"?ok")
        except:
                #Algo no ha ido bien, redireccionamos a Fai
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})