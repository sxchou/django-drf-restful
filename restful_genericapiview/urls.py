from django.urls import path, re_path

from restful_genericapiview import views

urlpatterns = [
    path('publish/', views.PublishView.as_view()),
    re_path(r'publish/(?P<pk>\d+)', views.PublishDetailView.as_view()),
]
