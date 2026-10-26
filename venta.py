class Venta:
    def __init__(self, id_venta, fecha, usuario, cliente=None):
        self.__id_venta = id_venta
        self.__fecha = fecha
        self.__total = 0.0
        self.__items = []
        self.__usuario = usuario
        self.__cliente = cliente

    @property
    def id_venta(self):
        return self.__id_venta

    @id_venta.setter
    def id_venta(self, valor):
        self.__id_venta = valor

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        self.__fecha = valor

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, valor):
        self.__total = valor

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, valor):
        self.__items = valor

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, valor):
        self.__usuario = valor

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):
        self.__cliente = valor

    def agregar_item(self, producto, kg):
        if kg <= 0:
            raise ValueError("La cantidad en kg debe ser mayor a 0.")
        if kg > producto.stock_kg:
            raise ValueError(f"Stock insuficiente de {producto.nombre}.")
        self.__items.append((producto, kg))

    def calcular_total(self):
        self.__total = sum(p.precio_kg * kg for p, kg in self.__items)
        return self.__total

    def registrar_venta(self):
        if not self.__items:
            return False
        self.calcular_total()
        for producto, kg in self.__items:
            producto.stock_kg = producto.stock_kg - kg
        return True

    def generar_recibo(self):
        lineas = [
            "===== RECIBO DE VENTA =====",
            f"Venta No.: {self.__id_venta}",
            f"Fecha: {self.__fecha}",
            f"Atendió: {self.__usuario.nombre}",
        ]
        if self.__cliente:
            lineas.append(f"Cliente: {self.__cliente.nombre}")
        lineas.append("-" * 28)
        for producto, kg in self.__items:
            subtotal = producto.precio_kg * kg
            lineas.append(f"{producto.nombre}: {kg} kg x ${producto.precio_kg:.2f} = ${subtotal:.2f}")
        lineas.append("-" * 28)
        lineas.append(f"TOTAL: ${self.calcular_total():.2f}")
        return "\n".join(lineas)

    def generar_corte(self, fecha):
        if self.__fecha == fecha:
            return self.calcular_total()
        return 0.0

    def mostrar_corte(self, fecha):
        print(f"Corte del {fecha}: ${self.generar_corte(fecha):.2f}")
