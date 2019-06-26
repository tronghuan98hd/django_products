class Product:
    def __init__(self, form=None):
        if form != None:
            self.id = form['id']
            self.code = form['code']
            self.name = form['name']
            self.description = form['description']
            self.unitPrice = form['unit_price']
    def toJson(self):
        product = {
            'id' : self.id,
            'code' : self.code,
            'name' : self.name,
            'description' : self.description,
            'unitPrice' : self.unitPrice
        }
        return product