from django.shortcuts import render

# Create your views here.
def ice(request):
    d={'name':'ice','price':50}
    return render (request,'ice.html',d)