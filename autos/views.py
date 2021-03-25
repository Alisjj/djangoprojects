from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Auto, Cat, Breed, Make
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "autos/main.html")


class AutosView(LoginRequiredMixin ,View):
    def get(self, request):
        ac = Auto.objects.all()
        cc = Make.objects.all().count()

        ctx = { 'make_count': cc, 'autos_list': ac }

        return render(request, "autos/auto_list.html", ctx)

class  CatView(LoginRequiredMixin, View):
    def get(self, request):
        ac = Cat.objects.all()
        cc = Breed.objects.all().count()

        ctx = { 'breed_count': cc, 'cat_list': ac }

        return render(request, "autos/cat_list.html", ctx)

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:autos_list')

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('autos:cat_list')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:autos_list')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('autos:cat_list')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:autos_list')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('autos:cat_list')

class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()

        ctx = { 'make_list': ml }
        return render(request, "autos/make_list.html", ctx)

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        bl = Breed.objects.all()

        ctx = { 'breed_list': bl }
        return render(request, "autos/breed_list.html", ctx)

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:autos_list')

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('autos:cat_list')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:autos_list')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('autos:cat_list')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:autos_list')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('autos:cat_list')
