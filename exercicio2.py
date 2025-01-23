class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"Produto {self.name} - R${self.price}"
    
    def discount(self, perc_discount):
        valorDiscount = (self.price/100 * perc_discount)
        finalPrice = self.price - valorDiscount
        return int(finalPrice)
        
xbox = Product("Xbox Series X", 4500)
print(xbox)
discont_xbox = xbox.discount(10)
print(f"Preco com desconto: ${discont_xbox}")