from typing import Any
from biblioteca import *

## Ejercicio 1

def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """ Agregar docstring acá
    """
    cantidad: int = 0
    for barco in barcos:
        if len(barco) == tamaño:
            cantidad += 1
    return cantidad
