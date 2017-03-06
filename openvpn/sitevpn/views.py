from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages, auth
from django.http import HttpResponseRedirect,HttpResponse
from django.core.mail import send_mail, EmailMultiAlternatives,BadHeaderError
from django.shortcuts import render_to_response,render,redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
from openvpn.forms import *
from openvpn.models import *
from django.template import Context
from django.utils.translation import ugettext as _
def home(request):
    return render(request, 'index.html')
@csrf_exempt
def contact1(request):
    subject = request.POST.get('subject', '')
    name=request.POST.get('name','')
    message = request.POST.get('message', '')
    from_email = request.POST.get('email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['vpnmongoliafree@@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')
def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            from_email = request.POST.get('email', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            body = 'Email: ' + from_email +''+ ', ' +'Name: '+name+''+ ',  ' + 'Message: ' + message + ''+'.'
            to_email = settings.EMAIL_HOST_USER
            try:
                send_mail(subject, body, from_email, ['vpnmongoliafree@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            return HttpResponse('Make sure all fields are entered and valid.')
    return render(request, "index.html", {'form': form})
def send_thanks(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')
    from_email = request.POST.get('from_email', '')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        return HttpResponse('Make sure all fields are entered and valid.')

def send_password_jap(request):
    subject,from_email='VpnMongolia Service. Your login and password.','vpnmongoliafree@gmail.com'
    to=request.user.email
    text_content='This email contains your login and password to the VPN. So save this email.'
    html_content='<p>Thank you using our <strong>VpnMongolia</strong> service. We sent you login and password to the access of OpenVPN Access Server.</p><br>Hostname (IP address with port number) : 153.127.249.210:943<br>Login: openvpnuser01269 <br>Password: vpnuser0169 <br><Br><br>Thank you. <br>VpnMongolia Service 2017. <br>Our website: www.mongol.world'
    msg=EmailMultiAlternatives(subject,text_content,from_email,[to])
    msg.attach_alternative(html_content,"text/html")
    msg.send()
    return HttpResponseRedirect('/send/thanks/')
