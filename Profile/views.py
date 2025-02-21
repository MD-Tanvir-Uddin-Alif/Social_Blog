from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from Post.models import Post_Model
from .import models
from .import forms

# Create your views here.

class User_Profile_View(CreateView):
    model = models.User_profile
    form_class = forms.User_profile_Form
    template_name = 'Sign_Up_Form.html'
    success_url = reverse_lazy('Home_page')

    def form_valid(self, form):
        user = form.save()
        models.User_profile.objects.create(
            user = user,
            phone_number = form.cleaned_data.get('phone_number'),
            profile_picture = form.cleaned_data.get('profile_picture')
        )

        return redirect(self.success_url)
    

class CustomLoginView(LoginView):
    def get_success_url(self):
        return reverse_lazy('User_Profile')
    

class User_Profile_Details_View(LoginRequiredMixin, DetailView):
    model = models.User_profile
    template_name = 'profile.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return models.User_profile.objects.get(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_posts = Post_Model.objects.filter(Author = self.request.user)
        context['posts'] = user_posts
        return context
        

class User_Profile_Edit_View(LoginRequiredMixin,UpdateView):
    model = models.User_profile
    form_class = forms.User_Profile_Edit_Form
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('User_Profile')

    def get_object(self):
        return self.request.user.user_profile
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user_instance'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)