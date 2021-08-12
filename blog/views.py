from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from .models import Artile,Category
def index(request):
    articles_list=Artile.objects.published()
    paginator = Paginator(articles_list, 3)
    page = request.GET.get('page')
    article = paginator.get_page(page)
    context={
        'article':article,
        'category': Category.objects.all
    }

    return render (request,'blog/index.html',context)
def page(request,slug):
    context={
        'articles':get_object_or_404(Artile,slug=slug,status='p'),
    }
    return render(request,'blog/page.html',context)
def category(request,slug):
    context={
        'category': get_object_or_404(Category, slug=slug,status='True'),
    }
    return render(request,'blog/category.html',context)

def new(request):
    context={
        'new':Artile.objects.all
    }
    return render(request,'blog/new.html')
