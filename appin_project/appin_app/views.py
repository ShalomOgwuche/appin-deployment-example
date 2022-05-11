from django.shortcuts import render
from django.http import HttpResponse
from appin_app.models import Topic, AccessRecord, Webpage

# Create your views here.
def home(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dictionary = {'access_records':webpages_list}
    return render(request,'appin_app/index.html',context=date_dictionary)
