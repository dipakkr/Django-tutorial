from django.shortcuts import render, get_object_or_404

from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
    ListView
)

from .forms import ArticleModelForm
from .models import Article


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() # <blog>/<modelname>_list.html
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return '/'


class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() # <blog>/<modelname>_list.html


# using function to defin
def ArticleDetailView(request, _id):
    article = get_object_or_404(Article, id=_id)

    context = {
        "title" : article.title,
        "description" : article.description
    }

    return render(request, "articles/article_detail.html", context)


# class ArticleDetailView(DetailView):
#     template_name = 'articles/article_detail.html'
#     queryset = Article.objects.all()

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Article, id=id_)


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
