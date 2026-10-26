class Usuario:
    def __init__(self, id_usuario, nombre, usuario, contrasena, rol):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__usuario = usuario
        self.__contrasena = contrasena
        self.__rol = rol

    @property
    def id_usuario(self):
        return self.__id_usuario

    @id_usuario.setter
    def id_usuario(self, valor):
        self.__id_usuario = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, valor):
        self.__usuario = valor

    @property
    def contrasena(self):
        return self.__contrasena

    @contrasena.setter
    def contrasena(self, valor):
        self.__contrasena = valor

    @property
    def rol(self):
        return self.__rol

    @rol.setter
    def rol(self, valor):
        self.__rol = valor

    def iniciar_sesion(self, usuario, contrasena):
        return self.__usuario == usuario and self.__contrasena == contrasena

    def es_admin(self):
        return self.__rol.lower() == "admin"

    def agregar_usuario(self):
        return True

    def modificar_usuario(self):
        return True

    def eliminar_usuario(self):
        return True

    def mostrar_usuario(self):
        print(f"ID: {self.__id_usuario}")
        print(f"Nombre: {self.__nombre}")
        print(f"Usuario: {self.__usuario}")
        print(f"Rol: {self.__rol}")
