from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Product,Name,Orders
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')
def index(request):
    product = Product.objects.all()
    print(product)

    
    co_name = Product.get_all_name()
    cats = {item["comp_name"] for item in co_name}
    name = list(cats)
    
    if request.method=="GET":
        st=request.GET.get('company_name')
        if st != None:
            product = Product.objects.filter(product_name__icontains=st)


        
    param = {'product':product,'name':name  }  
    return render(request,'phone/index.html',param)

def about(request):
    return render(request,'phone/about.html')

def viewcheck(request,myid):
    product= Product.objects.filter(product_id=myid)
    return render(request,'phone/viewcheck.html',{'product':product[0]})


@login_required(login_url='signin')
def home(request):
    return render(request,'phone/home.html')


def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(request,username=username,password=pass1)

        if user is not None:
            login(request,user)
            
            return redirect('mobileview')
        else:
            return HttpResponse("<h1 align='center' style='color:black;background-color:red' ;border:'rounded'><pre>Your username and password is wrong !<br><br>try again..</h1></pre>")
    

    return render(request,'phone/signin.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        if pass1!=pass2:
            return HttpResponse("your password is not same.")
        else:
            myuser = User.objects.create_user(username,email,pass1)
            myuser.firstname = fname
            myuser.lastname = lname
            myuser.save()
            messages.success(request,"your account has been successfully creat") 
            return redirect('signin')
    
    
    return render(request,'phone/signup.html')

def signout(request):
    logout(request)
    messages.success(request,"logged out Successfully")

    return redirect('signin')

def checkout(request):
    if request.method=="POST":
        items_json= request.POST.get('itemsJson', '')
        name=request.POST.get('name', '')
        email=request.POST.get('email', '')
        address=request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city=request.POST.get('city', '')
        state=request.POST.get('state', '')
        zip_code=request.POST.get('zip_code', '')
        phone=request.POST.get('phone', '')

        order = Orders(items_json= items_json, name=name, email=email, address= address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank=True
        id=order.order_id
        return render(request, 'phone/checkout.html/', {'thank':thank, 'id':id})
    return render(request,'phone/checkout.html')





