from django.urls import path,re_path
from restful_mixins import views
urlpatterns = [
    path('students/', views.StudentView.as_view()),
    re_path(r'students/(?P<pk>\d+)', views.StudentDetailView.as_view()),
]

