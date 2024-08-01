from django.urls import path
from .views import BlogDeleteView,HomePageView,BlogUpdateView, AboutPageView,BlogPageView,BlogDetailView,BlogCreateView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('about/', AboutPageView.as_view(), name='about'),
path('blog/', BlogPageView.as_view(), name='blog'),
path('blog/new/', BlogCreateView.as_view(), name='blog_new'),
path('blog/<int:pk>/edit/',BlogUpdateView.as_view(), name='blog_edit'),
path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
path('blog/<int:pk>/delete/',BlogDeleteView.as_view(), name='blog_delete'),

]