from .views import register_view, profile
from django.urls import path

urlpatterns = [

    path('signup', register_view),
    path('profile', profile),

]
