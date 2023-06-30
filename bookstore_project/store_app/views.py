from django.shortcuts import render
from .models import AuthorModel,BookModel,ReviewModel
from .forms import AuthorForm,BookForm,ReviewForm

# Create your views here.
def home(request):
    authors = AuthorModel.objects.all()

    if request.method == "GET":
        author_name = request.GET.get('author_name')
        if author_name:
            books = BookModel.objects.filter(author__name__icontains=author_name)
        else:
            books = BookModel.objects.all()
    else:
        books = BookModel.objects.all()
    
    context = {
        "author":authors,
        "books":books
    }
    return render(request,"home.html",context)
    
def author(request):
    if request.method == "POST":
        data = AuthorForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            msg = "Author Saved"
            fm = AuthorForm()
            return render(request,"author.html",{"fm":fm,"msg":msg})
        else:
            msg = data        
            return render(request,"author.html",{"msg":msg})
    else:
        fm = AuthorForm()
        return render(request,"author.html",{"fm":fm})
    
def book(request):
    if request.method == "POST":
        data = BookForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()
            msg = "Book created"
            fm = BookForm()
            return render(request,"book.html",{"fm":fm,"msg":msg})
        else:
            msg = data        
            return render(request,"book.html",{"msg":msg})
    else:
        fm = BookForm()
        return render(request,"book.html",{"fm":fm})
    
def book_detail(request,id):
    book = BookModel.objects.get(id=id)
    reviews = ReviewModel.objects.filter(book=book)
    if request.method == "POST":
        data = ReviewForm(request.POST)
        if data.is_valid():
            new_data = data.save(commit=False)
            new_data.book = book
            new_data.save()
            fm = ReviewForm()
            return render(request,'book_detail.html',{"fm":fm,"reviews":reviews,"book":book})
        else:
            msg = data
            return render(request,'book_detail.html',{"msg":msg,"reviews":reviews,"book":book})
    else:
        fm = ReviewForm()
        return render(request,'book_detail.html',{"fm":fm,"reviews":reviews,"book":book})