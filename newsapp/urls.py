from django.urls import path
# Импортируем созданное нами представление
from .views import PostList


urlpatterns = [

   path('', PostList.as_view()),
   ]