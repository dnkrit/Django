from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Главная страница</h1>")

def data_view(request):
    return HttpResponse("<h1>Страница Data</h1>")

def test_view(request):
    return HttpResponse("<h1>Страница Test</h1>")
