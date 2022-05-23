from django.urls import path

from .views import BookApiView

urlpatterns = [
    path('api/', BookApiView.as_view()),
]
