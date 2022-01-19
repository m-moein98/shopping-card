from django.urls import path

from .views import CardView

urlpatterns = [
    path('', CardView.as_view(), name="card"),
    path('<int:id>', CardView.as_view()),
]
