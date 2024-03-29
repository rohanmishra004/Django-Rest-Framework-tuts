from django.contrib import admin
from django.urls import path , include
from rest_framework import routers

from quickstart import views

router= routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'Groups',views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns+=router.urls
