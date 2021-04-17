from django.shortcuts import render
from myapp import analysis
from myapp import cityanalysis
from myapp import wordcloud

def index(request):
    return render(request,'index.html')

def home(request):
    dropdown=list(set(analysis.zomato_india['City']))
    context={'dropdown':dropdown}
    return render(request,'main.html',context)

def cities(request,pk):
    cityanalysis.getcitydata(pk)
    cityanalysis.getcuisine(pk)
    cityanalysis.competitor(pk)
    wordcloud.getwordcloud(pk)
    dropdown=list(set(analysis.zomato_india['City']))
    context={
        'city':pk,
        'dropdown':dropdown
    }
    return render(request,'citywise.html',context)
