from django.shortcuts import render

# Create your views here.
def product(request):
    productId = request.POST.get('productId','1001')
    productName = request.POST.get('productName', 'world')
    productPrice = request.POST.get('productPrice', '12000')
    return render(request, 'product.html',
    {'productId': productId, 'productName': productName, 'productPrice': productPrice})

def index(request):
    products = [
        {
        'productId':'1001',
        'productName': 'MISC',
        'productPrice': '12000'
    },
    {
        'productId':'1002',
        'productName': 'HANDY',
        'productPrice': '11000'
    }
]
    return render(request, 'index.html', {'products' : products})
   
