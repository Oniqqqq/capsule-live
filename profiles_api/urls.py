from django.urls import path, include
from push_notifications.api.rest_framework import APNSDeviceAuthorizedViewSet
from rest_framework.routers import DefaultRouter
from profiles_api import views
from django.conf.urls import url

router = DefaultRouter()
router.register(r'openedcapsules', views.OpenedCapsuleListViewSet, basename='OpenedListCapsule')
router.register(r'closedcapsules', views.ClosedCapsuleListViewSet, basename='ClosedListCapsule')


urlpatterns = [
    path('', include(router.urls)),
    path('capsuledetail/<int:pk>/', views.CapsuleDetail.as_view(), name='halo'),
    path('existuser/<str:name>/', views.ExistUser.as_view(), name='existuser'),
    path('addimage/<int:pk>/', views.AddImageView.as_view(), name='createimage'),
    path('rest-auth/resend-verification-email/', views.ResendEmailVerification.as_view(),
         name='rest_resend_verification_email'),
    url(r'^capsule/$', views.CapsuleCreateAPIView.as_view(), name='createcapsule'),

    url(r'^device/apns/?$', APNSDeviceAuthorizedViewSet.as_view({'post': 'create'}), name='create_apns_device'),


]
