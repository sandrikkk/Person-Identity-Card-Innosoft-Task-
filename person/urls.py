from django.urls import path
from person import views

urlpatterns = [
    path("", views.PersonsIdentity.as_view())
]
