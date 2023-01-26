from distutils.command.upload import upload
from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from App_Flow.models import  moviedata
import os

# Create your views here.

def home(request):
    return render (request , 'index.html')



def movie(request):
    return render (request, 'movie.html')


def moviesum(request):
    if request.method == 'POST':
        data = moviedata()
        data.movie_name = request.POST.get('Fname')
        data.movie_id = request.POST.get('Fid')
        data.movie_rating = request.POST.get('Fprice')
        data.movie_description = request.POST.get('Fdescription')
        if len(request.FILES)!= 0:
            data.movie_image = request.FILES['Fimage']
        data.save()
        return redirect('/movie')

def showdata(request):
    newdata = moviedata.objects.all()
    return render(request , 'showdata.html', {'newdata' : newdata})
    
def editdata(request,pk):
    data = moviedata.objects.get(id=pk)
    if request.method == 'POST':
        if len(request.FILES)!=0:
            if len(data.movie_image)>0:
                os.remove(data.movie_image.path)
            data.movie_image = request.FILES['Fimage']
        data.movie_name = request.POST.get('Fname')
        data.movie_id = request.POST.get('Fid')
        data.movie_rating = request.POST.get('Fprice')
        data.movie_description = request.POST.get('Fdescription')
        data.save()
        return redirect("/")
    context = {'data': data}
    return render(request, 'editpage.html',  context )

def deletedata(request,pk):
    data = moviedata.objects.get(id=pk)
    if len(data.movie_image) > 0:
        os.remove(data.movie_image.path)
    data.delete()
    return redirect('/')
        
        


        



