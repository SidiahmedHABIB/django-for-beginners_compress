from django.urls import path
from .views import BlogDeleteView,SignUpView,HomePageView,BlogUpdateView, AboutPageView,BlogPageView,BlogDetailView,BlogCreateView
from django.contrib.auth import views as auth_views

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('about/', AboutPageView.as_view(), name='about'),
path('blog/', BlogPageView.as_view(), name='blog'),
path('blog/new/', BlogCreateView.as_view(), name='blog_new'),
path('blog/<int:pk>/edit/',BlogUpdateView.as_view(), name='blog_edit'),
path('blog/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
path('blog/<int:pk>/delete/',BlogDeleteView.as_view(), name='blog_delete'),
path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
path('signup/', SignUpView.as_view(), name='signup'),

]