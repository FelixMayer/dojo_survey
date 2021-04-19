from django.urls import path, include 

from . import views

urlpatterns = [
	path("", views.main),
	path("form_submit", views.form_submit),
	path("result", views.result)
]