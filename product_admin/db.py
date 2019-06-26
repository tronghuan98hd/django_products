products=[]
def addProduct(code,name):
    if len(products)==0:
        id=1
    else:
        id=products[-1]['id'] + 1
    products.append({'code':code,'name':name,'id':id})
    return products
def getProducts():
    return products
def deleteProduct(id):
    for prod in products:
        if prod['id'] == id:
            products.remove(prod)
def updateProduct(id,code,name):
    product = findById(id)
    if product != None:
        product['code'] = code
        product['name'] = name
        return product
def findById(id):
    for prod in products:
        if prod["id"] == id:
            return prod


    