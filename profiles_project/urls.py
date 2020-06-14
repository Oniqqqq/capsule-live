from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views.static import serve
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from allauth.account.views import confirm_email, password_reset
from django.conf import settings
from profiles_api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls')),
    path('login/', views.LoginView.as_view(), name='rest_login'),
    path('password/reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email, name='account_confirm_email'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)', serve, {
            'document_root': settings.MEDIA_ROOT,
        })
    ]

