import json
from datetime import datetime


class CartItem:
    def __init__(self, name, price, quantity):
        if price < 0 or quantity < 0:
            raise ValueError("El precio y la cantidad deben ser valores positivos")
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_quantity(self, quantity):
        if quantity < 0:
            raise ValueError("La cantidad debe ser un valor positivo")
        self.quantity += quantity

    def to_dict(self):
        return {"name": self.name, "price": self.price, "quantity": self.quantity}


class ShoppingCart:
    def __init__(self):
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.subtotal = 0
        self.total = 0
        self.items = []

    def add_item(self, item):
        found = False
        for i in self.items:
            if i.name == item.name:
                i.add_quantity(item.quantity)
                found = True
        if not found:
            self.items.append(item)
        self.subtotal += item.price * item.quantity
        self.total = self.subtotal

    def remove_item(self, item):
        if item in self.items:
            self.subtotal -= item.price * item.quantity
            self.items.remove(item)
        self.total = self.subtotal

    def calculate_total(self):
        self.total = self.subtotal

    def save_to_json(self, filename):
        data = {
            "date": self.date,
            "subtotal": self.subtotal,
            "total": self.total,
            "items": [i.to_dict() for i in self.items],
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filename):
        with open(filename, "r") as f:
            data = json.load(f)
            self.date = data["date"]
            self.subtotal = data["subtotal"]
            self.total = data["total"]
            self.items = [
                CartItem(i["name"], i["price"], i["quantity"]) for i in data["items"]
            ]


carrito_nuevo = ShoppingCart()
carrito_nuevo.add_item(CartItem("Minna No Nihongo 1", 29990, 1))
carrito_nuevo.add_item(CartItem("Minna No Nihongo 1", 29990, 1))
carrito_nuevo.add_item(CartItem("Minna No Nihongo 1", 29990, 1))
carrito_nuevo.add_item(CartItem("Minna No Nihongo 1", 29990, 1))
carrito_nuevo.add_item(CartItem("Minna No Nihongo 1", 29990, 1))
carrito_nuevo.add_item(CartItem("Minna No Nihongo 1", 29990, 1))
carrito_nuevo.calculate_total()
carrito_nuevo.save_to_json("muchos_minna_no_nihongo.json")
