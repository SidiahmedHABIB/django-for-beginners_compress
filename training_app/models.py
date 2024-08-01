from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Add any additional fields here

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    
    # Add related_name to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change related_name to avoid clashes
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions '
                   'granted to each of their groups.'),
        related_query_name='customuser',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change related_name to avoid clashes
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_query_name='customuser',
    )

class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    def get_absolute_url(self): 
        return reverse('blog_detail', args=[str(self.id)])
