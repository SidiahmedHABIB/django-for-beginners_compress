from django.urls import path
from .views import HomePageView, AboutPageView,BlogPageView,BlogDetailView

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('about/', AboutPageView.as_view(), name='about'),
path('blog/', BlogPageView.as_view(), name='blog'),
path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),

]