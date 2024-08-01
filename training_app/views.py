from django.views.generic import TemplateView ,ListView
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_posts_list' # new


class AboutPageView(TemplateView):
    template_name = 'about.html'
