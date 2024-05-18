from django.shortcuts import render, get_list_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm

class RecipeListView(ListView):
    model = Recipe
    template_name ='recipes/templates/recipe_list.html'
    context_object_name ='recipes'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        difficulty = self.request.GET.get('difficulty')

        if query:
            queryset = queryset.filter(title__icontains=query) | queryset.filter(ingredients__icontains=query)

        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)

        return queryset.order_by('-id')

class RecipeDetailView(DetailView):
    model = Recipe
    template_name ='recipes/recipe_detail.html'

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name ='recipes/recipe_form.html'
    success_url = reverse_lazy('recipes:recipe_list')

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name ='recipes/recipe_form.html'
    success_url = reverse_lazy('recipes:recipe_list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name ='recipes/recipe_confirm_delete.html'
    success_url = reverse_lazy('recipes:recipe_list')

