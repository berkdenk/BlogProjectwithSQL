from typing import Any
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

from theBlog.models import Profile
from .forms import SignUpForm,EditProfileForm,ProfilePageForm
from django.contrib.auth.views import PasswordChangeView,PasswordChangeForm
from django.urls import reverse_lazy

class CreateProfilePageView(CreateView):
    model=Profile
    template_name="registration/create_user_profile_page.html"
    #fields="__all__"
    form_class=ProfilePageForm

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
    

class UserRegisterView(generic.CreateView):
    form_class=SignUpForm
    template_name='registration/register.html'
    success_url=reverse_lazy('login')

class ShowProfilePageView(DetailView):
    model=Profile
    template_name='registration/user_profile.html'

    def get_context_data(self, **kwargs):
        #users=Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(**kwargs)

        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context


class EditProfilePageView(generic.UpdateView):
    model=Profile
    template_name='registration/edit_profile_page.html'
    fields=['bio','profile_pic','fb_url','twitter_url','instagram_url']
    success_url=reverse_lazy('home')

"""class PasswordChangeView(PasswordChangeView):
    form_class=PasswordChangeForm
    success_url=reverse_lazy('home')

    def get_context_data(self, **kwargs):
        users=Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(**kwargs)

        page_user=get_object_or_404(Profile,id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context"""
    

class UserEditView(generic.UpdateView):
    form_class=EditProfileForm
    template_name='registration/edit_profile.html'
    success_url=reverse_lazy('home')

    def get_object(self):
        return self.request.user
