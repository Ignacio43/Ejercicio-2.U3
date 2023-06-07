
class Helado:
    def __init__(self, gramos, precio, sabor=None):
        self.__gramos = gramos
        self.__precio = precio
        self.__sabores = []
        if sabor is not None:
            self.add_sabor(sabor)

    def get_precio(self):
        return self.__precio

    def add_sabor(self, sabor):
        self.__sabores.append(sabor)

    def get_gramos(self):
        return self.__gramos 

    def get_sabores(self):
        return self.__sabores

    def __str__(self):
        return f"Helado: {self.__gramos} gr, Precio: {self.__precio}"