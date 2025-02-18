"""
URL configuration for coolsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# from games.views import index
# from games.views import categories
# from games.views import *
from django.urls import path, include
#from coolsite import settings
# from games.views import page_not_found

from coolsite import settings
from games.views import page_not_found

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('games/', index),
    # path('categories/', categories )
    path('', include('games.urls'))
]

# ТОЛЬКО ДЛЯ ОТЛАДОЧНОГО РЕЖИМА
# к маршрутам urlpatterns добавится еще 1 маршрут(к загруженным файлах)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_rppt=settings.MEDIA_ROOT)

handler404 = page_not_found
