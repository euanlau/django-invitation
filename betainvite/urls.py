from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView

from betainvite.views import invite, waitlist_signup

urlpatterns = patterns('',
    url(r'^invite/complete/$',
        TemplateView.as_view(template_name='betainvite/invitation_complete.html'),
        name='invitation_complete'),
    url(r'^invite/$',
        invite,
        name='invitation_invite'),
    url(r"^beta/signup/$",
        waitlist_signup,
        name="waitlist_signup"),
    url(r"^beta/signup/success/$",
        TemplateView.as_view(template_name="betainvite/waitlist_success.html"),
        name="waitlist_success"),
)
