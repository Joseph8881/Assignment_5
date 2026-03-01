
from django.contrib import admin
from django.urls import path
from puzzle.views import puzzle_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', puzzle_view),
]