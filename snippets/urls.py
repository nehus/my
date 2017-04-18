from django.conf.urls import url

from snippets.views import *
from snippets import models
from . import views


app_name = 'snippets'
urlpatterns = [
    # url(r'^snippets/$', UserSignUp.as_view(),name='UserSignUp'),
    url(r'^$', views.UserSignUp, name='UserSignUp'),
    #url(r'^otp$', views.OTP,name='OTP'),
    # url(r'^otp/$', views.OTP, name='OTP'),
    url(r'^(?P<temp_id>[0-9]+)/$', views.OTP, name='OTP'),
    url(r'^login/$', views.Login, name='Login'),
    # url(r'^resend_otp/$', views.resend_otp, name='resend_otp'),
    url(r'^(?P<temp_id>[0-9]+)/resend_otp/$', views.resend_otp, name='resend_otp'),
]


