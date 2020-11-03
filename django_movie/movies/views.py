from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from .forms import ReviewForm



class MovieView(ListView):
    """Список фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft =False)
    template_name = "movies/movie_list.html"


#def index(request):
#    movies = Movie.objects.all()
#    return render(request,"index.html",{"movie_list":movies})

#def some_file(request):
#    return render(request,"movies/some_file.html")

class MovieDetailView(DetailView):

    model = Movie
    slug_field = "url"


class AddReview(View):
    """Отзыв"""
    def post(self,request,pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent",None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save() 
        return redirect(movie.get_absolute_url())
