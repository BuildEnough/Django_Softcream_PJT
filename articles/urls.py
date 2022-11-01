from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [

    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('<int:pk>/update', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:user_pk>/user_page/', views.user_page, name='user_page'),
    path('category/', views.category, name='category'),  

]
