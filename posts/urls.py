from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostIndex.as_view(), name='index'),
    path('post_category/<str:category>',
         views.PostCategories.as_view(), name='post_categories'),
    path('busca/', views.PostSearch.as_view(), name='post_search'),
    path('post:<int:pk>', views.PostDetails.as_view(), name='post_index'),
]
