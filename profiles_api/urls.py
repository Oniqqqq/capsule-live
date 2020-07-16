from django.urls import path, include
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
    url(r'^capsule/$', views.CapsuleCreateAPIView.as_view(), name='createcapsule'),

]
