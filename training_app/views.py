from django.views.generic import DeleteView, UpdateView,TemplateView,CreateView ,ListView,DetailView
from .models import Post , Blog 
from django.urls import reverse_lazy # new
from .forms import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new


class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogPageView(ListView):
    model = Blog
    template_name = 'blog.html'

class BlogDetailView(DetailView): 
    model = Blog
    template_name = 'blog_detail.html'

class BlogCreateView(CreateView): 
    model = Blog
    template_name = 'blog_new.html'
    fields = '__all__'
class BlogUpdateView(UpdateView): 
    model = Blog
    template_name = 'blog_edit.html'
    fields = ['title', 'body']
class BlogDeleteView(DeleteView): 
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog')