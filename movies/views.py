from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'movies': ['La la land', 'Whiplash', 'School of Rock']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})




#expected folder structure for templates
    # app name/templates/app name/index.html *(template file

    # our case: movies/templates/movies/index.html

