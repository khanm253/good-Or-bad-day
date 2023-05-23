from django.urls import path

from . import views

urlpatterns = [
    path("goodOrbad", views.GoodOrBadAPIView.as_view(), name="good-or-bad"),
    path("goodOrbad/results", views.ResultsAPIView.as_view(), name="results"),
]