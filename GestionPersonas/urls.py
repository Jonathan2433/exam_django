"""GestionPersonas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from persona_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # persona_app URLS
    path('', views.persona_list, name="url_list"),
    path('list/', views.persona_list),
    path('details/<int:id>/', views.persona_details, name='persona_details'),
    path('create/', views.persona_create),
    path('generate/', views.generate_persona),
]
