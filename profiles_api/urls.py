from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views
from django.conf.urls import url


urlpatterns = [

    url(r'^capsule/$', views.CapsuleCreateAPIView.as_view(), name='createcapsule'),
    #url(r'^sharedto/$', views.SharedToViewSet.as_view(), name='shareto'),

]
