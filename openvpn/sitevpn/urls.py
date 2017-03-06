"""djangoopenvpn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views
from . import settings
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from openvpn.forms import Registrationform
from django.conf.urls.i18n import i18n_patterns
urlpatterns =i18n_patterns(
    url(r'^admin/', admin.site.urls),
	url(r'^$',views.home,name='home'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^openvpn/',include('openvpn.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^demo/windows/$',TemplateView.as_view(template_name='demo/windows.html'), name='demo-windows'),
    url(r'^demo/android/$',TemplateView.as_view(template_name='demo/android.html'), name='demo-android'),
	url(r'^demo/apple/$',TemplateView.as_view(template_name='demo/apple.html'), name='demo-apple'),
	url(r'^demo/iphone/$',TemplateView.as_view(template_name='demo/iphone.html'), name='demo-iphone'),
	url(r'^demo/mac/$',TemplateView.as_view(template_name='demo/mac.html'), name='demo-mac'),
    url(r'^demo/linux/$',TemplateView.as_view(template_name='demo/linux.html'), name='demo-linux'),
    url(r'^services/windows/$',TemplateView.as_view(template_name='services/windows.html'), name='service-windows'),
    url(r'^services/mac/$',TemplateView.as_view(template_name='services/mac.html'), name='service-mac'),
    url(r'^services/ios/$',TemplateView.as_view(template_name='services/iphone.html'), name='service-ios'),
    url(r'^services/android/$',TemplateView.as_view(template_name='services/android.html'), name='service-android'),
    url(r'^services/linux/$',TemplateView.as_view(template_name='services/linux.html'), name='service-linux'),
	url(r'^about/$',TemplateView.as_view(template_name='openvpn.html'), name='about'),
    url(r'^email/sendpass-jap/$', views.send_password_jap, name='send_password'),
    url(r'^email/$', TemplateView.as_view(template_name='email_pass.html'), name='email'),
    url(r'^send/thanks/$', TemplateView.as_view(template_name='thanks.html'), name='email'),
    url(r'^zohoverify/verifyforzoho.html', TemplateView.as_view(template_name='zohoverify/verifyforzoho.html'), name='zoho')

)+[
      url(r'^contacts/$',views.contact, name='contacts'),
    url(r'^contact/thanks/$', TemplateView.as_view(template_name='cont_thanks.html'), name='success'),
    ]

