import csv
from Sabor import Sabor

class ManejaSabores:
    def __init__(self):
        self.__sabores = []

    def cargar_sabores(self):
        with open("sabores.csv", newline='') as archivo:
            reader = csv.reader(archivo, delimiter=';')
            for fila in reader:
                id_sabor = int(fila[0])
                ingredientes = fila[1]
                nombre_sabor = fila[2]
                sabor = Sabor(id_sabor, ingredientes, nombre_sabor)
                self.__sabores.append(sabor)

    def retornaSabor(self,num_sabor):
        i=0
        while i<len(self.__sabores) and self.__sabores[i].get_id_sabor()!=num_sabor:
            i+=1
        if i<len(self.__sabores):
            return self.__sabores[i]
        


    def mostrar_sabores(self):
        for sabor in self.__sabores:
            print(f"ID: {sabor.get_id_sabor()}, Nombre: {sabor.get_nombre_sabor()}")