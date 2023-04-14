from django.urls import path, include
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog' ),
    path('table/', views.table, name= 'table'),
    path('blog/<int:post_id>', views.details, name='detail')
]