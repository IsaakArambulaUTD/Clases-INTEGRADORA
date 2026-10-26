from datetime import date


class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio_kg,
                 stock_kg, stock_minimo, fecha_caducidad):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__precio_kg = precio_kg
        self.__stock_kg = stock_kg
        self.__stock_minimo = stock_minimo
        self.__fecha_caducidad = fecha_caducidad

    @property
    def id_producto(self):
        return self.__id_producto

    @id_producto.setter
    def id_producto(self, valor):
        self.__id_producto = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @property
    def precio_kg(self):
        return self.__precio_kg

    @precio_kg.setter
    def precio_kg(self, valor):
        self.__precio_kg = valor

    @property
    def stock_kg(self):
        return self.__stock_kg

    @stock_kg.setter
    def stock_kg(self, valor):
        self.__stock_kg = valor

    @property
    def stock_minimo(self):
        return self.__stock_minimo

    @stock_minimo.setter
    def stock_minimo(self, valor):
        self.__stock_minimo = valor

    @property
    def fecha_caducidad(self):
        return self.__fecha_caducidad

    @fecha_caducidad.setter
    def fecha_caducidad(self, valor):
        self.__fecha_caducidad = valor

    def agregar(self):
        return True

    def modificar(self):
        return True

    def eliminar(self):
        return True

    def mostrar_inventario(self):
        print(f"ID: {self.__id_producto}")
        print(f"Nombre: {self.__nombre}")
        print(f"Descripción: {self.__descripcion}")
        print(f"Precio por kg: ${self.__precio_kg:.2f}")
        print(f"Stock: {self.__stock_kg} kg")
        print(f"Stock mínimo: {self.__stock_minimo} kg")
        print(f"Caducidad: {self.__fecha_caducidad}")

    def alerta_caducidad(self):
        dias = (self.__fecha_caducidad - date.today()).days
        if dias < 0:
            return f"¡{self.__nombre} está caducado!"
        if dias <= 7:
            return f"{self.__nombre} caduca en {dias} día(s)."
        return f"{self.__nombre}: caducidad en orden."

    def alerta_stock(self):
        if self.__stock_kg <= self.__stock_minimo:
            return (f"Stock bajo de {self.__nombre}: "
                    f"{self.__stock_kg} kg (mínimo {self.__stock_minimo} kg).")
        return f"{self.__nombre}: stock suficiente."
