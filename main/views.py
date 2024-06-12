from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView, CreateView
from main.forms import CommentForm
from main.models import Article, About, Tag, Comment
# Create your views here.


class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'articles'
    queryset = Article.objects.all().order_by('-id')[:7]


class ArticlesPageView(ListView):
    model = Article
    template_name = 'blog.html'
    context_object_name = 'articles'
    paginate_by = 3

    def get_queryset(self):
        return Article.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        article_list = Article.objects.all().order_by('-id')
        paginator = Paginator(article_list, self.paginate_by)

        page = self.request.GET.get('page')
        try:
            articles = paginator.page(page)
        except PageNotAnInteger:
            articles = paginator.page(1)
        except EmptyPage:
            articles = paginator.page(paginator.num_pages)

        context['articles'] = articles
        context['tags'] = Tag.objects.all()
        return context


class ArticleDetailPage(CreateView, DetailView):
    model = Article
    template_name = 'blog_single.html'
    context_object_name = 'post'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article_id=self.kwargs['pk']).order_by('-id')
        context['tags'] = self.request.GET.get('tags')
        return context

    def form_valid(self, form):
        post = self.get_object()
        comment = form.save(comment=False)
        comment.article = post
        comment.save()
        return redirect(f"/detail/{post.id}")


class AboutPageView(ListView):
    model = About
    template_name = 'about.html'
    context_object_name = 'abouts'
