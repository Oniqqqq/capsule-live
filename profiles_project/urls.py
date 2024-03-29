
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls import url

from django.conf import settings
from profiles_api import views
from rest_auth.views import PasswordResetConfirmView
from django.views.generic import TemplateView
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls')),
    path('login/', views.LoginView.as_view(), name='rest_login'),
    path('apple-app-site-association/', TemplateView.as_view(
        template_name='apple-app-site-association',
        content_type='application/json',
        )),
    re_path(
        r'^rest-auth/password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
   # url(r'^', include('django.contrib.auth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^verification=1/', TemplateView.as_view(template_name='index.html'),
        name='account_confirm_email'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]

