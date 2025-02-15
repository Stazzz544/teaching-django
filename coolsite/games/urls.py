from django.conf.urls import handler404
from django.urls import path, re_path

from .views import  *

#если в файле coolsite/coolsite/urls.py в path не '', то это будет добавлено
# к урлу

urlpatterns = [
    #name='home' - параметр маршрута
    path('', index, name='home'), #http://127.0.0.1:8000/

    path('categories/<int:id>/', categories ), #http://127.0.0.1:8000/categories/1

    path('categories-slug/<slug:game>/', categories_slug),
    # http://127.0.0.1:8000/categories/far_cry_3

    #сначала идет префикс archive, а дальше год из 4 цифр - ругялрка
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive)#
    # http://127.0.0.1:8000/categories/far_cry_3

]

