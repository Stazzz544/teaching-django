import json

from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .models import *


#для того, чтобы дёрнуть данные из базы


# Create your views here.
# ===========================
# Это функции представления
# ===========================

@csrf_exempt
def add(request):
    if request.method == 'POST':
        try:
            # Декодируем JSON-данные из тела запроса
            data = json.loads(request.body)

            # Проверяем, что все необходимые поля присутствуют
            required_fields = ['title', 'content', 'price', 'image']
            if not all(field in data for field in required_fields):
                return JsonResponse({'error': 'Missing required fields'}, status=400)

            # Создаем запись в базе данных
            game = Games(
                title=data['title'],
                content=data['content'],
                price=data['price'],
                image=data['image']
            )
            game.save()

            # Возвращаем успешный ответ
            return JsonResponse({
                'message': 'Product created successfully',
                'id': game.id  # Возвращаем ID созданной записи
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get(request):
    if request.method == 'GET':
        try:
            # Получаем все записи из базы данных
            products = Games.objects.all()

            # Сериализуем данные в список словарей
            product_list = []
            for product in products:
                product_list.append({
                    'id': product.id,
                    'title': product.title,
                    'content': product.content,
                    'price': str(product.price),  # DecimalField преобразуем в строку
                    'image': product.image.url if product.image else None
                    # Получаем URL изображения
                })

            # Возвращаем JSON-ответ
            return JsonResponse({
                'message': 'Success',
                'products': product_list
            }, status=200)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

menu = ["О сайте", "Добавить статью", "Обратная связь"]

def index(request):
    posts = Games.objects.all()
    return render(request, 'games/index.html', {
        'title': 'Главная страница',
        'menu': menu,
        'posts':posts
    })

def about(request):
    return render(request, 'games/about.html', {'title': 'О сайте', "menu": menu})


def categories(request, id):
    if request.GET:
        print(request.GET)

    if request.POST:
        print(request.POST)

    return HttpResponse(f"<h1>Страница приложения Games</h1>"
                        f"<p>Текущий id: {id}</p>")


# slug - буквы и цифры(латиница)
def categories_slug(request, game):
    return HttpResponse(f"<h1>Страница приложения Games</h1>"
                        f"<p>Текущий slug: {game}</p>")


def archive(request, year):
    # пример редиректа
    # по дефолту код редиректа 302 - временный редирект
    if int(year) == 2020:
        return redirect('home')  # тут параметр паршрута из urls.py

    # постоянный редирект с кодом 301 - permanent=True
    if int(year) > 2021:
        return redirect('home', permanent=True)

    # пример not found
    if int(year) > 2021:
        raise Http404()

    return HttpResponse(f"<h1>Страница приложения Games</h1>"
                        f"<p>Архив по годам: {year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

