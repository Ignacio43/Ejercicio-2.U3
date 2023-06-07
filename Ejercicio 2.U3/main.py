
from ManejadorHelado import ManejaHelados
from ManejadorSabores import ManejaSabores

if __name__ == '__main__':
    manejador_sabores = ManejaSabores()
    manejador_sabores.cargar_sabores()

    manejador_helados = ManejaHelados()

    print("1. Registrar un helado vendido")
    print("2. Mostrar los 5 sabores de helado más pedidos")
    print("3. Estimar total de gramos vendidos de un sabor")
    print("4. Mostrar sabores vendidos en un tamaño de helado")
    print("5. Calcular importe total recaudado por tipo de helado")

    op = int(input("Ingrese la opción elegida (0 para salir): "))
    
    while op!=0:
        

        if op == 1:
            gramos = float(input("Ingrese el gramaje del helado solicitado: "))
            precio = float(input("Ingrese el precio: "))
            helado = manejador_helados.registrar_helado(gramos, precio)
            manejador_sabores.mostrar_sabores()
            cant = int(input("Ingrese la cantidad de sabores: "))
            for i in range(cant):
                num_sabor = int(input("Ingrese el número del sabor: "))
                sabor = manejador_sabores.retornaSabor(num_sabor)
                helado.add_sabor(sabor)
        elif op == 2:
            sabores_mas_pedidos = manejador_helados.obtener_sabores_mas_pedidos()
            print("Los 5 sabores de helado más pedidos son:")
            for sabor in sabores_mas_pedidos:
                print(sabor)
        elif op == 3:
            num_sabor = int(input("Ingrese el número del sabor: "))
            estimacion_gramos = manejador_helados.estimar_gramos_vendidos(num_sabor)
            print(f"Estimación de gramos vendidos: {estimacion_gramos} gr")
        elif op == 4:
            tamano = float(input("Ingrese el tamaño del helado: "))
            print(f"Sabores vendidos en helados de {tamano} gr:")
            manejador_helados.mostrar_sabores_por_tamano(tamano)
        elif op == 5:
            importe_por_tipo = manejador_helados.calcular_importe_total_recaudado()
            print("Importe recaudado por tipo de helado:")
            for tamano, importe in importe_por_tipo.items():
                print(f"{tamano} gr: ${importe}")
        else:
            print("Opción inválida. Intente nuevamente.")
            
        op = int(input("Ingrese la opción elegida (0 para salir): "))