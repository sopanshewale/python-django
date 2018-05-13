from django.shortcuts import render
from django.http import HttpResponse
#from temperature.Temperature import Temperature
from temperature.models import Temperature
from temperature.forms import TemperatureForm
import random
from django.core.files.storage import FileSystemStorage
from temperature.forms import UploadFileForm
from django.conf import settings
 




def index(request):
    return render(request, 'index.html')

def about(request):
    temp_form = TemperatureForm()

    if request.method == 'GET':
       records = Temperature.objects.all()
       return render(request, 'about.html', {'temp_form': temp_form, 'records': records, }) 
    elif request.method == 'POST':
       form  = TemperatureForm (request.POST)
       print (form) 
       if form.is_valid():
          form.save()
       return render(request, 'about.html', {'temp_form': temp_form }) 
       


#def records (request):
#    pass
#
def records(request):
    weather_1 = Temperature(
                            temperature=random.randint(20,40), 
                            max_temp=random.randint(30,40), 
                            min_temp=random.randint(20,30),
                           )
    weather_2 = Temperature(
                            temperature=random.randint(20,40), 
                            max_temp=random.randint(30,40), 
                            min_temp=random.randint(20,30)
                           )
    weather_3 = Temperature(
                            temperature=random.randint(20,40), 
                            max_temp=random.randint(30,40), 
                            min_temp=random.randint(20,30)
                           )
    weather_4 = Temperature(
                            temperature=random.randint(20,40), 
                            max_temp=random.randint(30,40), 
                            min_temp=random.randint(20,30)
                           )
    weather_list = [weather_1, weather_2, weather_3, weather_4]  
    context = {
        'temp':weather_list
    }

    return render(request, 'weather.html', context) 

def iris(request):
   from subprocess import call
   status = call(["/anaconda/bin/python", "/UUsers/sopanshewale/lychee/lychee/scripts/plot_iris_dataset.py"])
   if status == 0:
      return render(request, 'iris_success.html')
   else: 
      return render(request, 'iris_fail.html')
      
   




def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        path= getattr(settings, 'MEDIA_ROOT')
        fs = FileSystemStorage(path)
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')


def special_case_2003(request):
    return render(request, 'index.html')
     

def year_archive(request, year=None):
    print (year)
    print ("I can use this variable anywhere")
    return render(request, 'index.html')

def month_archive (request, year=None, month=None):
    pass

def article_detail(request):
    pass

def calculate(request):
    if request.method == 'GET':
         return render(request, 'calculator.html') 
    else:
         m = int(request.POST['firstnumber']) 
         n =  int(request.POST['secondnumber']) 
         sum = m + n
         return render(request, 'calculator.html', {'sumation': sum, 'first': m, 'second': n}) 
