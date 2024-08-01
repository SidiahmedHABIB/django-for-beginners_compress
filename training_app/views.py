from django.views.generic import TemplateView ,ListView,DetailView
from .models import Post , Blog 

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