from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from . import views
from allauth.account.views import confirm_email, login, logout
import importlib
from allauth.socialaccount import providers

providers_urlpatterns = []

for provider in providers.registry.get_list():
    prov_mod = importlib.import_module(provider.get_package() + '.urls')
    providers_urlpatterns += getattr(prov_mod, 'urlpatterns', [])

urlpatterns=[
    url(r'^index$',views.index,name = 'index'),
    url(r'^landing$',views.landing,name='landing'),
    url(r'^create$',views.create,name='create'),
    url(r'^auth/', include(providers_urlpatterns)),
    url(r'^confirm-email/(?P<key>[-:\w]+)/$', confirm_email, name='account_confirm_email'),
    url(r'^$', login, name='account_login'),
    url(r'^logout/$', logout, name='account_logout'),
    url(r'^signup/$', login, name='account_signup'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
