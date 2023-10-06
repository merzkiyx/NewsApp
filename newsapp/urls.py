from django.urls import path
from .views import PostList, PostDetail
from .import views


urlpatterns = [

   path('', PostList.as_view()),
   path('<int:pk>', PostDetail.as_view()),
]