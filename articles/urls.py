from django.urls import path
from .views import (
    ArticleDetailView,
    ArticleEditView,
    ArticleDeleteView,
    ArticleListView,
    ArticleCreateView
)


urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/edit/', ArticleEditView.as_view(), name='article_edit'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
]