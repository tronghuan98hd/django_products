from django.shortcuts import render,redirect


from product_admin import db
# Create your views here.

def index(request):
    return render(request,'index.html',
    context={'products':db.getProducts()})

def saveProduct(request):
    id=request.POST['id']
    name = request.POST['name']
    code = request.POST['code']
    if id.strip()=='' :
        db.addProduct(code,name)
    else:
        db.updateProduct(int(id),code,name)
    return redirect('home')
def addProduct(request):
    return render(request,'product.html')
def editProduct(request,id):
    product =next((p for p in db.products if p['id']==id ),None)
    return render(request,'product.html',{'product':product})
def deleteProduct(request,id):
    db.deleteProduct(id)
    return redirect('home')