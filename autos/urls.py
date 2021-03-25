from django.urls import path
from . import views


app_name = "autos"

urlpatterns = [
        path('main/', views.MainView.as_view(), name='all'),
        path('aut/', views.AutosView.as_view(), name='autos_list'),
        path('create/', views.AutoCreate.as_view(), name='auto_create'),
        path('<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
        path('<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
        path('make_list/', views.MakeView.as_view(), name='make_list'),
        path('make_create/', views.MakeCreate.as_view(), name='make_create'),
        path('make/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
        path('make/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
        path('', views.CatView.as_view(), name='cat_list'),
        path('cat_create/', views.CatCreate.as_view(), name='cat_create'),
        path('cat/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
        path('cat/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
        path('breed_list/', views.BreedView.as_view(), name='breed_list'),
        path('breed_create/', views.BreedCreate.as_view(), name='breed_create'),
        path('breed/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
        path('breed/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]
