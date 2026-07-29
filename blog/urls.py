
from django.urls import path
from .views import(user_list,summarize_post_view,generate_post_view)

urlpatterns = [
    path('api/users/',user_list, name='user-list'),
    path('posts/summarize/', summarize_post_view, name='summarize'),
    path('posts/generate/',generate_post_view, name='generate-post'),
]