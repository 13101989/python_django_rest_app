from django.urls import path

from .views import tools


urlpatterns = [
    path("tools", tools.get_tools),
]
