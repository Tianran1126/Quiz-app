from django.urls import path 
from . import views

app_name='quiz'
urlpatterns=[path('',views.Question_View.as_view(),name='index'),
             path('<int:pk>/',views.Option_View.as_view(),name='option'),
             path('<int:question_id>/decision/',views.decision,name='decision'),
             path('result/',views.result,name='result')]


"""
app_name='polls'
urlpatterns=[path('',views.IndexView.as_view(),name='index'),
             path('specifics/<int:pk>/',views.DetailView.as_view(),name='detail'),
             path('<int:pk>/results/',views.ResultsView.as_view(),name='results'),
             path('<int:question_id>/vote/',views.vote,name='vote'),
]
"""
