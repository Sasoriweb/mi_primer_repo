import json
from datetime import datetime


class Item:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def get_precio_total(self):
        return self.precio * self.cantidad


class CarritoDeCompras:
    def __init__(self):
        self.fecha = datetime.now()
        self.subtotal = 0
        self.total = 0
        self.cantidad_items = 0
        self.items = {}

    def agregar_item(self, nombre, precio, cantidad):
        item = Item(nombre, precio, cantidad)
        self.items[nombre] = item
        self.actualizar_totales()

    def actualizar_totales(self):
        self.subtotal = sum(item.get_precio_total() for item in self.items.values())
        self.cantidad_items = sum(item.cantidad for item in self.items.values())
        self.total = self.subtotal

    def guardar_en_archivo(self, archivo):
        carrito_dict = {
            "fecha": str(self.fecha),
            "subtotal": self.subtotal,
            "total": self.total,
            "cantidad_items": self.cantidad_items,
            "items": {},
        }

        for nombre, item in self.items.items():
            item_dict = {"precio": item.precio, "cantidad": item.cantidad}
            carrito_dict["items"][nombre] = item_dict

        with open(archivo, "w") as f:
            json.dump(carrito_dict, f, indent=4)

    @classmethod
    def cargar_desde_archivo(cls, archivo):
        with open(archivo, "r") as f:
            carrito_dict = json.load(f)

        carrito = cls()
        carrito.fecha = datetime.fromisoformat(carrito_dict["fecha"])
        carrito.subtotal = carrito_dict["subtotal"]
        carrito.total = carrito_dict["total"]
        carrito.cantidad_items = carrito_dict["cantidad_items"]

        for nombre, item_dict in carrito_dict["items"].items():
            item = Item(nombre, item_dict["precio"], item_dict["cantidad"])
            carrito.items[nombre] = item

        return carrito


carrito_nuevo = CarritoDeCompras()
carrito_nuevo.agregar_item("Minna No Nihongo 1",29990, 1)
carrito_nuevo.agregar_item("Minna No Nihongo 1",29990, 1)
carrito_nuevo.agregar_item("Minna No Nihongo 1",29990, 1)
carrito_nuevo.agregar_item("Minna No Nihongo 1",29990, 1)
carrito_nuevo.agregar_item("Minna No Nihongo 1",29990, 1)
carrito_nuevo.agregar_item("Minna No Nihongo 1",29990, 1)
carrito_nuevo.actualizar_totales()
carrito_nuevo.guardar_en_archivo("muchos_minna_no_nihongo.json")