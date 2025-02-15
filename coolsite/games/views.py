from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import  redirect


# Create your views here.
#===========================
# Это функции представления
#===========================

def index(request):
    return HttpResponse("СтранSица приложения Games")

def categories(request, id):
    if request.GET:
        print(request.GET)

    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Страница приложения Games</h1>"
                        f"<p>Текущий id: {id}</p>")

#slug - бувы и цифры(латиница)
def categories_slug(request, game):
    return HttpResponse(f"<h1>Страница приложения Games</h1>"
                        f"<p>Текущий slug: {game}</p>")

def archive(request, year):

    #пример редиректа
    #по дефолту код редиректа 302 - временный редирект
    if int(year) == 2020:
        return redirect('home') #тут параметр паршрута из urls.py

    #постоянный редирект с кодом 301 - permanent=True
    if int(year) > 2021:
        return redirect('home', permanent=True)

    #пример not found
    if int(year) > 2021:
        raise Http404()

    return HttpResponse(f"<h1>Страница приложения Games</h1>"
                        f"<p>Архив по годам: {year}</p>")

def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")