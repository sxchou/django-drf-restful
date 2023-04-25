from django.urls import path, re_path

from restful_apiview import views

urlpatterns = [
    path("user/info/", views.UserInfoView.as_view()),
    re_path(r"user/info/(\d+)", views.UserInfoDetailView.as_view()),
    path("author/", views.AuthorView.as_view()),
    re_path(r"author/(\d+)", views.AuthorDetailView.as_view()),
]
