from django.shortcuts import render,redirect
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
        
        
    else:
        request.session['count']+= 1
    if 'count2' not in request.session:
        request.session['count2'] = 1
        
        
    else:
        request.session['count2']+= 2    
    return render(request,'index.html')
      
def index2(request):
    
        
    if 'count'  in request.session:
         del request.session['count']
    if 'coun2'  in request.session:
         del request.session['count2']    
    return redirect('/')




    
def index3(request):
    if 'count2' not in request.session:
        request.session['count2'] = 1
        
        
    else:
        request.session['count2']+= 2
        
    return render(request,'index.html')
def index4(request):
    
        
    
         
    
    return render(request,'index.html')
