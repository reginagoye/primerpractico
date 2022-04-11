
from django.contrib import admin
from django.urls import path
from app1.views import vista_familiares

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vistaFamiliares/', vista_familiares),
]
