from .views import *
from django.urls import include, path, re_path
from .views import ArticleView
urlpatterns = [
path('',ArticleView.as_view({'get':'list'}))
]