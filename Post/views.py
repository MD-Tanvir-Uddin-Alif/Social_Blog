from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from .import models
from .import forms
# Create your views here.

class Post_Create_View(LoginRequiredMixin, CreateView):
    model = models.Post_Model
    form_class = forms.Post_Create_Form
    template_name = 'post_Create.html'
    success_url = reverse_lazy('User_Profile')

    def form_valid(self, form):
        form.instance.Author = self.request.user
        return super().form_valid(form)


class Post_Update_View(LoginRequiredMixin, UpdateView):
    model = models.Post_Model
    form_class = forms.Update_Post_Form
    template_name = 'post_update_form.html'
    success_url = reverse_lazy('User_Profile')

    def get_object(self, queryset=None):
        post = super().get_object(queryset)

        if post.Author != self.request.user:
            raise PermissionDenied
        return post


class Post_Delete_View(LoginRequiredMixin, DeleteView):
    model = models.Post_Model
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('User_Profile')

    def get_object(self, queryset=None):
        post = super().get_object(queryset)

        if post.Author != self.request.user:
            raise PermissionDenied
        return post
    

class Post_List_View(ListView):
    model = models.Post_Model
    template_name = 'post_list.html'
    context_object_name = 'posts'
    paginate_by = 20

    def get_queryset(self):
        return models.Post_Model.objects.all().order_by('-created_at')
    

class Post_Detail_View(DetailView):
    model = models.Post_Model
    template_name = 'post_details.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = forms.Comment_Form()
        context['comments'] = models.Comment_Model.objects.filter(post=self.get_object())

        return context
    
    def post(self, request, *args, **kwargs):
        post = self.get_object()
        form = forms.Comment_Form(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
        
        context = self.get_context_data(**kwargs)
        context['comment_form'] = form
        return self.render_to_response(context)
    

class Post_Like_View(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(models.Post_Model, pk=pk)

        if request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return redirect('post_detail', pk=post.pk)