from django.shortcuts import render,HttpResponse,redirect
import sys
from .forms import *

sys.path.insert(0, 'Home\\face_identifiaction')
from main import result as r
# Create your views here.
def index(request):
   
 
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)
        names = request.FILES.getlist('Img')
        for f in request.FILES.getlist('Img'):

            request.FILES['Img'] = f
            form = ImgForm(request.POST, request.FILES)
            if form.is_valid():
                #form.save()
                pass
        r = face_check(request,names)
        if r:
            return render(request,"Match.html")
        else:
            return render(request,"nomatch.html")
    else:
        form = ImgForm()
        return render(request,'check.html', {'form': form})
 
 
def sucess(request):
    return HttpResponse('successfully uploaded')

def face_check(request,names):
    
    rpath = "media\\images\\"
    
    name =[]
    for i in names:
        name.append(str(i))
    id = rpath+name[0]  # path of id saved
    selfie = rpath+name[0] #path of selfie saved
    print(id,selfie)
    res = r(id,selfie)
    return res
    if res:
        return render(request,"Match.html")
    else:
        return HttpResponse("No Match")

    # res will contain the result if the faces match or not 