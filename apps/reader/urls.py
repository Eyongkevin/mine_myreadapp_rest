from django.urls import path 
from rest_framework import routers
from . import views

app_name = 'reader-urls'

router = routers.SimpleRouter() # DefaultRouter
router.register("", views.ReaderViewSet)

urlpatterns = [
    path("login/", views.Login.as_view(), name="reader-login"),
] + router.urls

# Router





