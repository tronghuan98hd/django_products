products = [
    {
        'id' : '1',
        'code' : '101',
        'name' : 'Dat',
        'description' : 'description',
        'unitPrice' : '1.0'
    },
    {
        'id' : '2',
        'code' : '102',
        'name' : 'Dat',
        'description' : 'description',
        'unitPrice' : '1.0'
    }
]

def getProducts():
    return products

def findById(id):
    for product in products:
        if int(product['id']) == id:
            return product

def findByCode(code):
    for product in products:
        if product['code'] == code:
            return product

def addEditproduct(product):
    if product.id == '':
        maxid = max(int(prd['id']) for prd in products)
        product.id = maxid + 1
        products.append(product.toJson())
    else:
        prod = findById(int(product.id))
        products[products.index(prod)] = product.toJson()

def deleteproduct(id):
    product = findById(id)
    products.remove(product)

def validate(product):
    errorList = []
    if product.id == '' and findByCode(product.code) != None:
        errorList.append('Product code already exists')
    if product.code == '':
        errorList.append('Product code can not be blank')
    if product.name == '':
        errorList.append('Product name can not be blank')
    if product.unitPrice == '':
        errorList.append('Unit price can not be blank')
    return errorList