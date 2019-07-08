from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect

def index(request):
    if request.method=="POST":
        return HttpResponseRedirect("/addUser")
    users = {'Users':User.objects.all()}
    return render(request, "index.html", users)

def add_user(request):
    if request.method=="POST":
        tom=User()
        tom.name=request.POST.get("name")
        tom.age = request.POST.get("age")
        tom.save()
        return  HttpResponseRedirect("/")
    return render(request, "addUser.html")

def user_info(request):
    if request.GET.get('id',0) != 0 :
        request.session["id"] = request.GET['id']
    if request.method=="POST":
        return HttpResponseRedirect("/user/addBook")
    books={'Books':Book.objects.filter(user=User.objects.get(id=request.session.get("id"))), 'User':User.objects.get(id=request.session.get("id"))}
    return render(request,"books.html",books)

def add_book(request):
    if request.method=="POST":
        book=Book()
        book.name=request.POST.get("name")
        book.author = request.POST.get("author")
        book.user=User.objects.get(id=request.session.get("id"))
        book.save()
        return  HttpResponseRedirect("/user")
    user={'User':request.session.get("id")}
    return render(request, "addBook.html",user)

def book_change(request):
    if request.GET.get('idb',0) != 0:
        request.session['idb'] = request.GET['idb']
    book = Book.objects.get(id=request.session.get('idb'))
    if request.method=="POST":
        book.name=request.POST.get("name")
        book.author = request.POST.get("author")
        book.save()
        return HttpResponseRedirect("/user")
    books={'Book':book}
    return render(request,"changeBook.html",books)