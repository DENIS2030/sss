from django.urls import path


from . import views


urlpatterns =[
    #path('',views.index),
    path("",views.MovieView.as_view()),
    #path("some_file/",views.some_file),
    path("<slug:slug>/",views.MovieDetailView.as_view(),name="movie_detail"),
    path("review/<int:pk>/",views.AddReview.as_view(),name="add_review"),
]