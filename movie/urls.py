from django.urls import path
from .views import ActorView, MovieView

urlpatterns = [
       path('/actor', ActorView.as_view()),
       path('/movie', MovieView.as_view())
]

