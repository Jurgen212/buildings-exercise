# Edificios
## Jurgen Sanclemente
Hay 4 archivos principales, el main(), que simlemente empieza a ejecutar el contador_informacion.

El contador_informacion empieza generando una residencia.
La residencia se encarga de generar 3 unidades.
Cada que se cree una unidad, esta poseera 2 edificios.
Cada edificio crea dentro de si 8 pisos.
Cada piso posee 20 casas, que generan sus datos de forma aleatoria.

Todos los elementos son listas, que anexan los subelementos por medio de bucles for.
Luego al visualizar_data() solo recorremos las listas que ya han sido generadas.

Todas las funciones que generan elementos ( edificio, casa, unidad ) retornan el elemento ( lista ) con las sublistas contenidas.
# edificios-simena
