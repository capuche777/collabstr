from django.urls import path
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

app_name = 'creators'
urlpatterns = [
    path('', views.content_list, name='creators_list')
]

urlpatterns += router.urls
