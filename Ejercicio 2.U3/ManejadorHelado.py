from Helado import Helado
from Sabor import Sabor

class ManejaHelados:
    def __init__(self):
        self.__helados = []

    def registrar_helado(self, gramos, precio):
        helado = Helado(gramos, precio)
        self.__helados.append(helado)
        return helado

    def muestra_helados(self):
        for helado in self.__helados:
            print(helado)

    def obtener_sabores_mas_pedidos(self):
        sabores_pedidos = {}
        sabores_mas_pedidos2=[]
        for helado in self.__helados:
            for sabor in helado.get_sabores():
                if sabor in sabores_pedidos:
                    sabores_pedidos[sabor] += 1
                else:
                    sabores_pedidos[sabor] = 1
        sabores_mas_pedidos = sorted(sabores_pedidos.items(), key=lambda x: x[1], reverse=True)[:5]
        for sabor, i in sabores_mas_pedidos:
            sabores_mas_pedidos2.append(sabor.get_nombre_sabor()+" "+str(i))
        return sabores_mas_pedidos2


    def estimar_gramos_vendidos(self, num_sabor):
        total_gramos = 0
        for helado in self.__helados:
            sabores = helado.get_sabores()
            for i in range(len(sabores)):
                if num_sabor == sabores[i].get_id_sabor() :
                    total_gramos+= helado.get_gramos()/len(sabores)
        return total_gramos 


    def mostrar_sabores_por_tamano(self, tamano):
        sabores_vendidos = set()
        for helado in self.__helados:
            if helado.get_gramos() == tamano:
                sabores = helado.get_sabores()
                for sabor in sabores:
                    sabores_vendidos.add(sabor.get_nombre_sabor())
        for sabor in sabores_vendidos:
            print(sabor)

    def calcular_importe_total_recaudado(self):
        tipo_helados = {100: 0, 150: 0, 250: 0, 500: 0, 1000: 0}
        for helado in self.__helados:
            gramos = helado.get_gramos()
            importe = helado.get_precio()
            tipo_helados[gramos] += importe
        return  tipo_helados