from django.urls import path

from .views import (
    ChildrenHandler
)

urlpatterns = [
    path('', ChildrenHandler.as_view()),
]
