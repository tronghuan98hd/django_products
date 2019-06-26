from django.shortcuts import render, redirect
from . import form, db

def index(request):
    return render(request, 'index.html', {'products' : db.getProducts()})

def saveProduct(request):
    product = form.Product(request.POST)
    errorList = db.validate(product)
    if len(errorList) == 0:
        db.addEditproduct(product)
        return redirect('home')
    return render(request, 'add_edit_product.html', {'product' : product, 'errorList' : errorList})

def deleteProduct(request, id):
    db.deleteproduct(id)
    return redirect('home')

def editProduct(request, id):
    product = db.findById(id)
    return render(request, 'add_edit_product.html', {'product' : product})
