from django.shortcuts import render
from .models import Post

Posts = [
    {
        'author': 'Pritom Bhowmik',
        'title': 'Deep Learning',
        'content': 'Artificial Neural Network',
        'date_posted': 'August 29, 2020'
    },

    {
        'author': 'Andrew Ng',
        'title': 'Todays Machine Learning',
        'content': 'Machine Learning is a new Electricity',
        'date_posted': 'August 25, 2020'

    },

    {
        'author': 'Denial Roy',
        'title': 'AI in the edge of Developmnet',
        'content': 'Data Science, Machine Learning, Deep Learning',
        'date_posted': 'March 22, 2020'

    }

]


def home(request):
    context = {
        'Posts': Post.objetcs.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
