from django.urls import path

from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleUpdateView
)

from .views import ArticleDetailView

app_name = 'articles'

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/', ArticleDetailView, name='article-detail'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='article-update'),
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
]
