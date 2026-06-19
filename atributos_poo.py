class Producto:

    impuesto = 0.12
    total_creados = 0

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        Producto.total_creados += 1


#METODO DE INSTANCIA
    def precio_con_impuesto(self):
        return self.precio * (1 + self.impuesto)
    
    @classmethod 
    def cambiar_impuesto(cls, nuevo):
        if not (0 < nuevo < 1 ):
            raise ValueError ("El impuesto debe estar entre 0 y 1")
        cls.impuesto = nuevo




p1 = Producto("Laptop", 850.0)
p2 = Producto("Mouse", 25.5)

Producto.cambiar_impuesto(-5)


print(p1.nombre)
print(p1.impuesto)

print(f"Total Productos {Producto.total_creados}")

p1.impuesto = 0.15

print (f"El impuesto del producto 1: {p1.impuesto}")
print (f"El impuesto del producto 2: {p2.impuesto}")

print (f"El impuesto del producto 1: {p1.impuesto}")
print (f"El impuesto del producto 2: {p2.impuesto}")

print (p1.precio_con_impuesto)