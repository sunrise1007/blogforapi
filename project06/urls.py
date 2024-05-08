"""
URL configuration for project06 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app06 import views
from app07 import views as v1
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singer', views.SingerViewSet, basename='singer')
router.register('song', views.SongViewSet, basename='song')
router.register('carModel', views.CarModelViewSet, basename='carModel')
router.register('fuelType', views.FuelTypeViewSet, basename='fuelType')
router.register('car', views.CarViewSet, basename='car')
router.register('ceo', views.CeoViewSet, basename='ceo')

router1 = DefaultRouter()

router1.register('person', v1.PersonViewSet, basename='person')
router1.register('group', v1.GroupViewsSet, basename='group')
router1.register('membership', v1.MembershipViewSet, basename='membership')
router1.register('place', v1.PlaceViewSet, basename='place')
router1.register('restaurant', v1.RestaurantViewSet, basename='restaurant')
router1.register('waiter', v1.WaiterViewsSet, basename='waiter')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('api2/', include(router1.urls)),
]
