from typing import Any
from biblioteca import *

separacion: str = "--------------------------------------------------"

## Ejercicio 1

def cantidadDeBarcosDeTamaño(barcos: list[BarcoEnGrilla], tamaño: int) -> int:
    """ 
    Indica la cantidad de barcos de tamaño 'tamaño' que hay en 'barcos'.
    
    PRE: sonBarcosValidos(barcos)
    
    Args:
        barcos (list[BarcoEnGrilla]): Lista de barcos ubicados en la grilla.
        tamaño (int): Tamaño del barco que queremos contar.
        
    Returns:
        Cantidad de barcos de tamaño 'tamaño' en 'barcos'.
    """
    cantidad: int = 0
    for barco in barcos:
        if len(barco) == tamaño:
            cantidad += 1
    return cantidad

print(cantidadDeBarcosDeTamaño([
[('H', 3), ('H', 4), ('H', 5)],
[('F', 4), ('E', 4)],
[('B', 4), ('B', 3), ('B', 2)]
],2))
print(separacion)

# Ejercicio 2

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """
    Describe un nuevo estado de juego a partir de la 'cantidadDeFilas', de 
    la 'cantidadDeColumnas' y de los barcos en 'barcosDisponibles'.
    
    PRE: 1 <= cantidadDeFilas <= 26
    PRE: cantidadDeColumnas > 0
    PRE: |barcosDisponibles| > 0
    
    Args:
        cantidadDeFilas (int): La cantidad de filas de cada una de las grillas.
        cantidadDeColumnas (int): La cantidad de columnas de cada una de las grillas.
        barcosDisponibles (list[Barco]): Lista de barcos.
    
    Returns:
        Las dimensiones de las grillas, los barcos disponibles, el turno de quien es y los tableros del jugador 1 y 2.
    """
    return ((cantidadDeFilas, cantidadDeColumnas), barcosDisponibles, [UNO], nuevoTablero(cantidadDeFilas, cantidadDeColumnas), nuevoTablero(cantidadDeFilas, cantidadDeColumnas))
    #return((5,5), [3, 3, 2], [UNO],
    #         ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
    #          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
    #          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
    #         [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
    #          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
    #          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
    #         ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
    #          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
    #          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
    #         [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
    #          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
    #          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
    # )

def nuevoTablero(cantidadDeFilas: int, cantidadDeColumnas: int) -> Tablero:
    grilla: Grilla = []

    for elem in range(cantidadDeFilas):
        res: list[Celda] = []
        for elem in range(cantidadDeColumnas):
            res.append(VACÍO)
        grilla.append(res)

    return (grilla, grilla)

print(nuevoJuego(5, 5, [3,3,2]))


## Ejercicio 3

def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """ Indica si el estadoDeJuego es válido.
        El estadoDeJuego es válido si: el tablero tiene entre 1 y 26 filas, proque hay 26 letras en el abecedario.
                                       el tablero tiene al menos 1 columna.
                                       solo puede jugar un jugador a la vez.
                                       hay al menos un barco disponible en el juego.
                                       el tablero de jugador UNO es válido.
                                       el tablero de jugador DOS es válido.
                                       los ataques registrados entre tableros coinciden.
    """
    #res: bool = cantidadDeFilasEstadoJuego(estadoDeJuego) >= 1 and cantidadDeFilasEstadoJuego(estadoDeJuego) <= 26 and cantidadDeColumnasEstadoJuego(estadoDeJuego) > 0 and len(estadoDeJuego[2]) == 1 and len(barcosDisponibles(estadoDeJuego)) > 0 and tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, UNO), estadoDeJuego) and tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, DOS), estadoDeJuego) and coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego, UNO), tableroDeJugador(estadoDeJuego, DOS))
    # Verifica que en el juego haya entre 1 y 26 filas.
    hayEntre1y26Filas: bool = cantidadDeFilasEstadoJuego(estadoDeJuego) >= 1 and cantidadDeFilasEstadoJuego(estadoDeJuego) <= 26

    # Verifica que en el juego haya al menos una columna.
    hayAlMenosUnaColumna: bool = cantidadDeColumnasEstadoJuego(estadoDeJuego) > 0

    # Verifica que solo un jugador pueda jugar a la vez.
    soloUnJugadorALaVez: bool = len(estadoDeJuego[2]) == 1

    # Verifica que haya al menos un barco en el juego.
    hayAlMenosUnBarcoEnJuego: bool = len(barcosDisponibles(estadoDeJuego)) > 0

    # Verifica que el tablero del jugador UNO sea válido y cumpla con los requerimientos para tal.
    tableroDeJugadorUNOEsValido: bool = tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, UNO), estadoDeJuego)

    # Verifica que el tablero del jugador DOS sea válido y cumpla con los requerimientos para tal.
    tableroDeJugadorDOSEsValido: bool = tableroValidoEnJuego(tableroDeJugador(estadoDeJuego, DOS), estadoDeJuego)

    # Verifica que los ataques esten sincronizados entre tableros.
    losAtaquesCoinciden: bool = coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego, UNO), tableroDeJugador(estadoDeJuego, DOS))

    return hayEntre1y26Filas and hayAlMenosUnaColumna and soloUnJugadorALaVez and hayAlMenosUnBarcoEnJuego and tableroDeJugadorUNOEsValido and tableroDeJugadorDOSEsValido and losAtaquesCoinciden


def tableroValidoEnJuego(tablero: Tablero, estadoDeJuego: EstadoJuego) -> bool:
    res: bool = grillaVálidaEnJuego(grillaLocal(tablero), estadoDeJuego) and grillaVálidaEnJuego(grillaOponente(tablero), estadoDeJuego) and coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego), grillaLocal(tablero))


def coincidenBarcosEnGrilla(barcos: list[Barco], grilla: Grilla) -> bool:
    # Indica si varios barcos pertenecientes a la misma grilla tienen el mismo tamaño.
    return mismosElementos(barcos, tamaños(barcosEnGrilla[grilla]))


def tamaños(barcos: list[BarcoEnGrilla]) -> list[int]:
    # Indica cuál es el tamaño de cada uno de los barcos pertenecientes a la grilla.
    res: list[int] = []

    for barco in barcos:
        tamaño: int = len(barco)
        res.append(tamaño)

    return res


def mismosElementos(lista1: list[Any], lista2: list[Any]) -> bool:
    # Indica si dos listas tienen los mismos elementos.
     for elemento in lista1:
        return cantidadDeApariciones(elemento, lista1) == cantidadDeApariciones(elemento, lista2)


def coincidenPosicionesAtacadas(tablero: Tablero, tableroOponente: Tablero) -> bool:
    # Indica si las posiciones atacadas entre ambos tableros coinciden en contenido y cantidad.
    grilla_local = tablero[0]
    grilla_op_local = tableroOponente[0]
    grilla_op = tablero[1]
    grilla_op_op = tableroOponente[1]
    
    n1 = 0  # celdas no vacías en tablero1
    n2 = 0  # celdas no vacías en tableroOponente1
    
    filas = len(grilla_local)
    columnas = len(grilla_local[0])
    
    for i in range(filas):
        for j in range(columnas):
            celda_tablero = grilla_local[i][j]
            celda_tablero_op = grilla_op_local[i][j]
            celda_tableroOponente = grilla_op[i][j]
            celda_tableroOponente_op = grilla_op_op[i][j]
            
            if celda_tablero != VACÍO and celda_tablero != celda_tableroOponente_op:
                return False
            
            if celda_tableroOponente != VACÍO and celda_tableroOponente != celda_tablero_op:
                return False
            
            if celda_tablero != VACÍO:
                n1 += 1
            if celda_tableroOponente != VACÍO:
                n2 += 1
    
    return 0 <= n1 - n2 <= 1

tableroJ1 = ([
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [BARCO,VACÍO,VACÍO,VACÍO],
 [BARCO,VACÍO,BARCO,VACÍO],
 [VACÍO,VACÍO,BARCO,VACÍO]
],[
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [VACÍO,VACÍO,VACÍO,VACÍO]
 ])
tableroj2 = ([
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [VACÍO,BARCO,BARCO,BARCO],
 [VACÍO,VACÍO,VACÍO,VACÍO]
 ],[
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [VACÍO,VACÍO,VACÍO,VACÍO],
 [VACÍO,VACÍO,VACÍO,VACÍO]
 ])
verificacion = esEstadoDeJuegoVálido(((4,4), [2,2], [DOS], tableroJ1, tableroj2))
print(verificacion)
print(separacion)


## Ejercicio 4

def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """
    Realiza un disparo en la posición indicada, modificando el estado del juego según el resultado.

    REQUIERE:
        - juegoVálido:
            esEstadoDeJuegoVálido(estadoDeJuego)
        - laPosiciónEsVálidaEnLaGrilla:
            esPosiciónVálidaEnGrilla(posición,
                grillaOponente(tableroDeJugador(estadoDeJuego, turno(estadoDeJuego))))
        - posiciónNoAtacada:
            celdaEnPosición(grillaOponente(tableroDeJugador(estadoDeJuego, turno(estadoDeJuego))),
                posición) == VACÍO

    MODIFICA:
        - estadoDeJuego

    ASEGURA:
        - estadoJuegoSoloActualizaUnaCeldaYElTurno:
            Todas las componentes de estadoDeJuego permanecen iguales a sus respectivas
            componentes en estadoDeJuego@pre, excepto por:
              * La celda ubicada en la posición posición de la grilla del oponente del jugador
                turno(estadoDeJuego@pre), que siempre se modifica.
              * La celda ubicada en la misma posición de la grilla local del jugador atacado,
                que a veces se modifica.
              * El turno, donde turno(estadoDeJuego) distinto a turno(estadoDeJuego@pre).

        - disparoHaceAgua:
            Sea t2 el turno opuesto a turno(estadoDeJuego@pre).
            Si resultado = NADA, entonces:
                * celdaEnPosición(grillaLocal(tableroDeJugador(estadoDeJuego@pre, t2)), posición) == VACÍO
                * celdaEnPosición(grillaLocal(tableroDeJugador(estadoDeJuego, t2)), posición) == AGUA
                * celdaEnPosición(grillaOponente(tableroDeJugador(estadoDeJuego, turno(estadoDeJuego))),
                  posición) == AGUA

        - disparoAlBarco:
            Sea t2 el turno opuesto a turno(estadoDeJuego@pre).
            Si resultado = TOCADO, entonces:
                * celdaEnPosición(grillaLocal(tableroDeJugador(estadoDeJuego@pre, t2)), posición) == BARCO
                * celdaEnPosición(grillaLocal(tableroDeJugador(estadoDeJuego, t2)), posición) == BARCO
                * celdaEnPosición(grillaOponente(tableroDeJugador(estadoDeJuego, turno(estadoDeJuego))),
                  posición) == BARCO
    """
    # Determinar jugador actual y oponente
    jugador_actual = turno(estado_juego)
    jugador_oponente = UNO if jugador_actual == DOS else DOS

    # Obtener los tableros de ambos
    tablero_actual = tableroDeJugador(estado_juego, jugador_actual)
    tablero_oponente = tableroDeJugador(estado_juego, jugador_oponente)

    # Obtener las grillas relevantes
    grilla_oponente = grillaOponente(tablero_actual)
    grilla_local_oponente = grillaLocal(tablero_oponente)

    # Ver qué hay en la posición objetivo
    celda_objetivo = celdaEnPosición(grilla_local_oponente, posición)

    # Caso 1: Hay barco → TOCADO
    if celda_objetivo == BARCO:
        cambiarCeldaGrilla(grilla_oponente, posición, BARCO)
        resultado = TOCADO
    # Caso 2: Agua → NADA
    else:
        cambiarCeldaGrilla(grilla_oponente, posición, AGUA)
        cambiarCeldaGrilla(grilla_local_oponente, posición, AGUA)
        resultado = NADA

    # Cambiar el turno al otro jugador
    cambiarTurno(estado_juego)

    return resultado


## Ejercicio 5

def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    resultado: list[BarcoEnGrilla] = []
    filas: int = len(grilla)
    columnas: int = len(grilla[0])

    letras: list[str] = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    agregadas: list[list[bool]] = [[False for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            pos: Posición = (letras[i], j + 1)
            if grilla[i][j] == BARCO and not agregadas[i][j]:
                barco: BarcoEnGrilla = []

                if sePuedeConstruirBarcoHorizontalDesde(grilla, pos):
                    k: int = j
                    while k < columnas and grilla[i][k] == BARCO:
                        barco.append((letras[i], k + 1))
                        agregadas[i][k] = True
                        k += 1

                elif sePuedeConstruirBarcoVerticalDesde(grilla, pos):
                    k = i
                    while k < filas and grilla[k][j] == BARCO:
                        barco.append((letras[k], j + 1))
                        agregadas[k][j] = True
                        k += 1

                else:
                    barco.append(pos)
                    agregadas[i][j] = True

                resultado.append(barco)

    return resultado


def noHayMasDeUnaFormaDeConstruirUnBarcoDesde(grilla: Grilla, posición: Posición) -> bool:
    return not(sePuedeConstruirBarcoHorizontalDesde(grilla, posición)) or not(sePuedeConstruirBarcoVerticalDesde(grilla, posición))


def sePuedeConstruirBarcoHorizontalDesde(grilla: Grilla, posición: Posición) -> bool:
    return celdaEnPosición(grilla, posición) == BARCO and (hayBarcoAl(grilla, posición, DERECHA) or hayBarcoAl(grilla, posición, IZQUIERDA))


def sePuedeConstruirBarcoVerticalDesde(grilla: Grilla, posición: Posición) -> bool:
    return celdaEnPosición(grilla, posición) == BARCO and (hayBarcoAl(grilla, posición, ARRIBA) or hayBarcoAl(grilla, posición, ABAJO))


def posicionesOcupadasEnGrilla(grilla: Grilla, posiciones: list[Posición]) -> bool:
    for posición in posiciones:
        if celdaEnPosición(grilla, posición) != BARCO:
            return False
    return True

def algúnBarcoOcupaLaPosición(barcos: list[BarcoEnGrilla], posición: Posición) -> bool:
    for barco in barcos:
        if posición in barco:
            return True
    return False

barcos = [[('H', 3), ('H', 4), ('H', 5)],
 [('F', 4), ('E', 4)],
 [('B', 4), ('B', 3), ('B', 2)]]

print(algúnBarcoOcupaLaPosición(barcos, ('H',5)))
print(algúnBarcoOcupaLaPosición(barcos, ('E',5)))

grilla: list[list[Celda]] = [
    [BARCO, VACÍO, VACÍO],
    [VACÍO, BARCO, VACÍO],
    [VACÍO, VACÍO, BARCO]
]
posiciones1: list[Posición] = [('A',1), ('B',2), ('C',3)]
posiciones2: list[Posición] = [('A',1), ('B',2), ('C',3), ('A',2)]
print(posicionesOcupadasEnGrilla(grilla, posiciones1))
print(posicionesOcupadasEnGrilla(grilla, posiciones2))
print(separacion)

grilla: Grilla = [
[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
[BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
[BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
[VACÍO, BARCO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO],
]

print(barcosEnGrilla(grilla))
