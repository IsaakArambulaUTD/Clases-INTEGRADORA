class Cliente:
    def __init__(self, id_cliente, nombre, telefono):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__telefono = telefono

    @property
    def id_cliente(self):
        return self.__id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        self.__id_cliente = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, valor):
        self.__telefono = valor

    def registrar(self):
        return True

    def mostrar_datos(self):
        print(f"ID: {self.__id_cliente}")
        print(f"Nombre: {self.__nombre}")
        print(f"Teléfono: {self.__telefono}")
