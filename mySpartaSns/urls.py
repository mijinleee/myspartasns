from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("test/", views.base_response, name="first_test"),
    path("first/", views.first_view, name="fist_name"),
    path("", include("user.urls")),  # user앱의 url과 spartasns의 url을 연결해 주는 것
    path("", include("tweet.urls")),  # user앱의 url과 spartasns의 tweet 연결해 주는 것
]
