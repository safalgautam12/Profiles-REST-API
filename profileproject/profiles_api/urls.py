from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from profiles_api import views 


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
#if queryset is defined then we don't need to provide basename
router.register('profile',views.UserProfileVieset)
urlpatterns=[
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
    
]