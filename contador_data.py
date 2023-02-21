from g_residencias import generar_residencia


def visualiza_data():

    residencias = generar_residencia()
    contador = 1

    for residencia in residencias:
        for edificio in residencia:
            for piso in edificio:
                for casa in piso:
                    print("Numero Casa ", contador, " -> ", casa)
                    contador += 1
            print(" cambio de piso \n")
        print("Cambio edificio \n\n")
    print("Cambio residencia \n\n\n")


def contador_informacion():
    numero_habitantes_totales = 0
    numero_litros_totales = 0
    numero_energia_totales = 0

    residencias = generar_residencia()

    for residencia in residencias:
        for edificio in residencia:
            for piso in edificio:
                for casa in piso:
                    numero_habitantes_totales += casa["#"]
                    numero_litros_totales += casa["lt"]
                    numero_energia_totales += casa["kw"]

    print("En total hay ", numero_habitantes_totales, " de habitantes")
    print("En total se consumieron ", numero_litros_totales, " litros de agua")
    print("En total se consumieron ", numero_energia_totales, " de kw")
