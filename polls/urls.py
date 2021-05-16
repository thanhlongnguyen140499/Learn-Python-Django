from django.urls import path

from . import views
import polls

app_name = 'polls'
urlpatterns = [
    # ex : /polls/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # added the word 'specifics', // change urls 
    path('specifics/<int:pk>/', views.DetailView.as_view(), name='detail'),
]