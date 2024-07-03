from django.shortcuts import render
from django.contrib import messages
from .forms import ReviewForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Category
from .forms import MovieSearchForm
from .models import Movie
from .forms import MovieForm
from django.contrib.auth.decorators import login_required

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'home.html', {'categories': categories})

def movie_list(request):
    movies = Movie.objects.all()  # Default queryset, all movies
    search_form = MovieSearchForm(request.GET)  # Initialize form with GET data

    context = {
        'movies': movies,
        'search_form': search_form,
    }
    return render(request, 'movie_list.html', context)

def movie_list(request):
    movies = Movie.objects.all()
    search_form = MovieSearchForm(request.GET)
    
    query = request.GET.get('query')
    category = request.GET.get('category')
    
    if query:
        movies = movies.filter(title__icontains=query)
    
    if category:
        movies = movies.filter(category__name=category)
    
    context = {
        'movies': movies,
        'search_form': search_form,
    }
    return render(request, 'movie_list.html', context)
  

def movie_profile(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    reviews = movie.reviews.all()  # Assuming 'reviews' is the related_name used in the ForeignKey

    context = {
        'movie': movie,
        'reviews': reviews,
    }

    return render(request, 'movie_profile.html', context)

@login_required
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.added_by = request.user
            movie.save()
            return redirect('movie_detail', pk=movie.pk)
        else:
            # Print form.errors to console or log to inspect validation errors
            print(form.errors)
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})

@login_required
def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    reviews = movie.reviews.all()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.movie = movie
            new_review.user = request.user
            new_review.save()
            messages.success(request, 'Thank you for your review!')
            return redirect('movie_detail', pk=pk)
    else:
        form = ReviewForm()

    context = {
        'movie': movie,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'movie_detail.html', context)

@login_required
def edit_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit_movie.html', {'form': form, 'movie': movie})

@login_required
def delete_movie(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home')  # Redirect to home or another page after deletion
    return render(request, 'delete_movie.html', {'movie': movie})
def home(request):
    movies = Movie.objects.all()  # Retrieve all movies from the database
    return render(request, 'home.html', {'movies': movies})
# Create your views here.
