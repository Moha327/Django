from django.shortcuts import render, redirect 
def index(request):
    return render(request,"show.html")
        
def create_user(request):
    # this is the route that processes the form
    
    name_from_form = request.POST['name']
    email_from_form = request.POST['email']
    dojo_location = request.POST['location']
    favorite_language= request.POST['language'],
    comment= request.POST['comm']
    context = {
    	"name_on_template" : name_from_form,
    	"email_on_template" : email_from_form,
        "dojo_location" : dojo_location,
        "favorite_language" : favorite_language,
        "comment":comment
    }
    return render(request,"success.html",context)
def success(request):
    # this is the success route
    return render(request,"success.html")