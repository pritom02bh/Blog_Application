from django.shortcuts import render

post = [
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

    }

]


def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')
