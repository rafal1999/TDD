from django.shortcuts import render,redirect
from django.http import HttpResponse
from lists.models import Item
# Create your views here. '</html><title>To do list</title></html>'


def home_page(request):
    if request.method=='POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')
    
    # items = Item.objects.all() niepotrzebne 
    return render(request,'home.html',) 
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html',{'items':items})
