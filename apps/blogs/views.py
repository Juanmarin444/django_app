from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    context = {
        "email" : "blog@gmail.com",
        "name" : "mike"
    }
    return render(request, "blogs/index.html", context) # ADD the name of your app ("blogs") so django know where to find the templates

def new(request):
    response = "Placeholder to later display a new form to create a new blog."
    return HttpResponse(response)

def create(request):
    print("THIS CREATED A NEW BLOG!")
    if request.method == "POST":
        print("*" * 50)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test" 
        print("*" * 50)
        return redirect("/")
    else:
        return redirect("/")

def show(request,number):
    response = "Placeholder to later display blog " + number
    return HttpResponse(response)

def edit(request, number):
    response = "Placeholder to later edit blog " + number
    return HttpResponse(response)

def destroy(request, number):
    print("BLOG NUMBER " + number + " HAS BEEN DESTROYED!")
    return redirect('/')