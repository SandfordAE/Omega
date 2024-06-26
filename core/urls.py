from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name='index'),
    # path("__debug__/", include("debug_toolbar.urls")),
    path("about/", views.about, name="about"),
    path("accounts/", include("allauth.urls")),
    path("demo/", include("demo.urls")),
    path("contact/", views.contact, name="contact"),
    path("licensing/", views.licensing, name="licensing"),
    path("overview/", views.overview, name="overview"),
    path("privacy_policy/", views.privacy_policy, name="privacy_policy"),

]
