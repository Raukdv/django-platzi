"""
URL configuration for platzi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include

from django.conf.urls import (
handler400, handler403, handler404, handler500
)

urlpatterns = [
    path('admin/', admin.site.urls),
]

#Modules Urls
urlpatterns += [
    path(
        '',
        include(('polls.urls', 'polls'), namespace='polls')
    )
]

#Handlers
handler400 = 'polls.views.error.pag_400_bad_request'
handler403 = 'polls.views.error.pag_403_forbidden'
handler404 = 'polls.views.error.pag_404_not_found'
handler500 = 'polls.views.error.pag_500_error_server'