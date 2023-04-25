from django.urls import path, include
from rest_framework import routers

from restful_modelviewset import views

router = routers.DefaultRouter()
router.register('book', views.BookView)
urlpatterns = [
    path("", include(router.urls)),
]
