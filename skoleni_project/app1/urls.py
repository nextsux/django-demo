from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from app1 import views as v

router = routers.SimpleRouter()
router.register(r'customer', v.CustomerViewSet)


urlpatterns = [
    url(r'^zakaznici$', v.CustomerList.as_view(), name='vypis-zakazniku'),
    url(r'^api/', include(router.urls)),
]
