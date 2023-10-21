from typing import Any, Dict
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,EditForm

#listview= query for me and bring data for list on page
#Deatailview=bring like one record

#def home(request):
#    return render(request,"home.html",{})



class HomeView(ListView):
    model=Post
    template_name='home.html'
    ordering=['-post_date']

    def get_context_data(self, **kwargs):
        cat_menu=Category.objects.all()
        context = super(HomeView,self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context

def CategoryListView(request):
    cat_menu_list=Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})


def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-',' ') , 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'

    def get_context_data(self, **kwargs):
        cat_menu=Category.objects.all()
        context = super(ArticleDetailView,self).get_context_data(**kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class AddPostView(CreateView):
    model = Post
    form_class=PostForm
    template_name='add_post.html'
    #fields='__all__'
    #fields=('title','body')
    
class AddCategoryView(CreateView):
    model = Category
    #form_class=PostForm
    template_name='add_category.html'
    fields='__all__'
    #fields=('title','body')

class UpdatePostView(UpdateView):
    model=Post
    template_name='update_post.html'
    form_class=EditForm
    #fields=['title','title_tag','body']

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')
    