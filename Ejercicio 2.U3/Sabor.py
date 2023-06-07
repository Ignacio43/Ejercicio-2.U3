class Sabor:
    def __init__(self, id_sabor, ingredientes, nombre_sabor):
        self.__id_sabor = id_sabor
        self.__ingredientes = ingredientes
        self.__nombre_sabor = nombre_sabor

    def get_id_sabor(self):
        return self.__id_sabor

    def get_nombre_sabor(self):
        return self.__nombre_sabor