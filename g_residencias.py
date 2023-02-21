from g_casa import generar_casa


def generar_piso():
    piso_de_20_casas = []

    for i in range(0, 20):
        piso_de_20_casas.append(generar_casa())

    return piso_de_20_casas


def generar_edificio():
    edificios = []

    for i in range(0, 8):
        edificios.append(generar_piso())

    return edificios


def generar_unidad():
    unidad = []

    for i in range(0, 2):
        unidad.append(generar_edificio())

    return unidad


def generar_residencia():
    residencias = []

    for i in range(0, 3):
        residencias.append(generar_unidad())

    return residencias
