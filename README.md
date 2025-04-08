# Listas Circulares

Este repositorio contiene implementaciones de listas circulares en Python.

## Descripción

Una lista circular es una estructura de datos en la cual el último nodo apunta al primer nodo, formando un ciclo. Este tipo de estructura es útil en aplicaciones donde se necesita un recorrido continuo de elementos.

En este proyecto, utilizamos listas circulares para emular la función de un reloj analógico. Un reloj analógico tiene una naturaleza cíclica, ya que las manecillas del reloj regresan a la posición inicial después de completar una vuelta completa (es decir, 12 horas para la manecilla de las horas, 60 minutos para la manecilla de los minutos, y 60 segundos para la manecilla de los segundos).

### Emulación de un Reloj Analógico

Para emular un reloj analógico con listas circulares, seguimos estos pasos:

1. **Lista Circular de Segundos**: Creamos una lista circular que contiene 60 nodos, uno para cada segundo. Cada nodo está numerado del 0 al 59. La manecilla de los segundos avanza de un nodo al siguiente cada segundo, y vuelve al nodo 0 después de alcanzar el nodo 59.

2. **Lista Circular de Minutos**: Similar a la lista de segundos, creamos una lista circular de 60 nodos para los minutos. La manecilla de los minutos avanza de un nodo al siguiente cada vez que la manecilla de los segundos completa una vuelta completa (60 segundos).

3. **Lista Circular de Horas**: Creamos una lista circular de 12 nodos para las horas. La manecilla de las horas avanza de un nodo al siguiente cada vez que la manecilla de los minutos completa una vuelta completa (60 minutos).

## Estructura del Proyecto

- `listasCirculares.py`: Contiene la implementación de la estructura de la lista circular.

## Requisitos

- Python 3.x

