from django.shortcuts import render
from django.http import HttpResponse
# Create your views here. '</html><title>To do list</title></html>'


def home_page(request):
    return render(request,'home.html',{'new_item_text': request.POST.get('item_text',''),}) 
