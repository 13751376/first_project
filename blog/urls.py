from django.urls import path
from . import views
app_name='blog'
urlpatterns =[
    path('',views.index,name='index'),
    path('article/<slug:slug>',views.page,name='page'),
    path('category/<slug:slug>',views.category,name='category'),
    path('new/',views.new,name='new'),
]
