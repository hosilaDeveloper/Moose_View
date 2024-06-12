from django.urls import path
from .views import HomePageView, ArticlesPageView, ArticleDetailPage, AboutPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('article/', ArticlesPageView.as_view(), name='articles'),
    path('detail/<int:pk>', ArticleDetailPage.as_view(), name='detail'),
    path('about/', AboutPageView.as_view(), name='about'),
]
