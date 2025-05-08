from django.shortcuts import render, redirect, get_object_or_404
from .models import News_post
from .forms import NewsForm

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def add_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Данные были заполнены некорректно"
    else:
        form = NewsForm()
    return render(request, 'news/add_new_post.html', {'form': form, 'error': error})

def news_detail(request, pk):
    news = get_object_or_404(News_post, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})
