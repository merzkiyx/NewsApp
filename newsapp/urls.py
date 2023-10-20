from django.urls import path
from .views import (
   PostList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch, ArticlesCreate, ArticlesUpdate, ArticlesDelete
)
from .import views


urlpatterns = [
   path('', PostList.as_view(), name = 'post_list'),
   path('<int:pk>', PostDetail.as_view(), name = 'post_detail'),
   path('news/create/', PostCreate.as_view(), name ='post_create'),
   path('news/<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('article/create/', ArticlesCreate.as_view(), name='articles_create'),
   path('article/<int:pk>/edit/', ArticlesUpdate.as_view(), name='article_update'),
   path('article/<int:pk>/delete/',ArticlesDelete.as_view(), name='article_delete'),
  ]