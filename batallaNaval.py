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

verificarEj1 = cantidadDeBarcosDeTamaño([
[('H', 3), ('H', 4), ('H', 5)],
[('F', 4), ('E', 4)],
[('B', 4), ('B', 3), ('B', 2)]
],2)
print(verificarEj1)
print(separacion)


# Ejercicio 2

def nuevoJuego(
        cantidadDeFilas: int,
        cantidadDeColumnas: int,
        barcosDisponibles: list[Barco]
    ) -> EstadoJuego:
    """
    Crea un nuevo estado de juego.
    
    PRE: cantidadDeFilas >= 1 ∧ cantidadDeFilas <= 26
         cantidadDeColumnas > 0
         |barcosDisponibles| > 0
         
    Args:
        cantidadDeFilas (int): Cantidad de filas que tendrá el tablero.
        cantidadDeColumnas (int) : cantidad de columnas que tendrá el tablero.
        barcosDisponibles (list[Barco]): lista de barcos, pero solo van a figurar el tamaño de los barcos.
    
    Returns:
        Un nuevo estado de juego 'EstadoJuego', donde ambos tableros 'Tablero' en 'EstadoJuego' comienzan vacios.
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

    for _ in range(cantidadDeFilas):
        res: list[Celda] = []
        for _ in range(cantidadDeColumnas):
            res.append(VACÍO)
        grilla.append(res)

    return (grilla, grilla)

print(nuevoJuego(5, 5, [3,3,2]))


## Ejercicio 5
# FUNCIONES AUXILIARES
def algúnBarcoOcupaLaPosición(barcos: list[BarcoEnGrilla], posición: Posición) -> bool:
    for barco in barcos:
        if posición in barco:
            return True
    return False

def posicionesOcupadasEnGrilla(grilla: Grilla, posiciones: list[Posición]) -> bool:
    for posición in posiciones:
        if celdaEnPosición(grilla, posición) != BARCO:
            return False
    return True

def sePuedeConstruirBarcoVerticalDesde(grilla: Grilla, posición: Posición) -> bool:
    return celdaEnPosición(grilla, posición) == BARCO and (hayBarcoAl(grilla, posición, ARRIBA) or hayBarcoAl(grilla, posición, ABAJO))

def sePuedeConstruirBarcoHorizontalDesde(grilla: Grilla, posición: Posición) -> bool:
    return celdaEnPosición(grilla, posición) == BARCO and (hayBarcoAl(grilla, posición, DERECHA) or hayBarcoAl(grilla, posición, IZQUIERDA))

def noHayMasDeUnaFormaDeConstruirUnBarcoDesde(grilla: Grilla, posición: Posición) -> bool:
    return not(sePuedeConstruirBarcoHorizontalDesde(grilla, posición)) or not(sePuedeConstruirBarcoVerticalDesde(grilla, posición))


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

# FUNCION PRINCIPAL
def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """ Devuelve todos los barcos que se encuentran dentro de la grilla.
    """
    res: list[BarcoEnGrilla] = []
    filas: int = len(grilla)
    columnas: int = len(grilla[0])

    letras: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    for i in range(filas):
        for j in range(columnas):
            posición: Posición = (letras[i], j+1)

            if grilla[i][j] == BARCO and not algúnBarcoOcupaLaPosición(res, posición):
                barco: BarcoEnGrilla = []

                if sePuedeConstruirBarcoHorizontalDesde(grilla, posición):
                    k: int = j
                    while k < columnas and grilla[i][k] == BARCO:
                        barco.append((letras[i], k+1))
                        k += 1
                    
                elif sePuedeConstruirBarcoVerticalDesde(grilla, posición):
                    k: int = i
                    while k < filas and grilla[k][j] == BARCO:
                        barco.append((letras[k], j+1))
                        k += 1
                
                else:
                    barco.append(posición)
                
                res.append(barco)

    return res

grilla: Grilla = [
[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
[BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
[BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
[VACÍO, BARCO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO],
]

verificarEj5 = barcosEnGrilla(grilla)
print(verificarEj5)


## Ejercicio 3
# FUNCIONES AUXILIARES
def coincidenPosicionesAtacadas(tablero: Tablero, tableroOponente: Tablero) -> bool:
    grilla_local = tablero[0]
    grilla_op_local = tableroOponente[0]
    grilla_op = tablero[1]
    grilla_op_op = tableroOponente[1]
    
    n1 = 0  # Celdas no vacías en tablero1
    n2 = 0  # Celdas no vacías en tableroOponente1
    
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

def mismosElementos(lista1: list[Any], lista2: list[Any]) -> bool:
    for elemento in lista1:
        if cantidadDeApariciones(elemento, lista1) != cantidadDeApariciones(elemento, lista2):
            return False
    return True

def tamaños(barcos: list[BarcoEnGrilla]) -> list[int]:
    res: list[int] = []

    for barco in barcos:
        tamaño: int = len(barco)
        res.append(tamaño)  

    return res

def coincidenBarcosEnGrilla(barcos: list[Barco], grilla: Grilla) -> bool:
    return mismosElementos(barcos, tamaños(barcosEnGrilla(grilla)))

def tableroVálidoEnJuego(tablero: Tablero, estadoDeJuego: EstadoJuego) -> bool:
    res: bool = grillaVálidaEnJuego(grillaLocal(tablero), estadoDeJuego) and grillaVálidaEnJuego(grillaOponente(tablero), estadoDeJuego) and coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego), grillaLocal(tablero))
    return res

# FUNCION PRINCIPAL
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
    tableroDeJugadorUNOEsValido: bool = tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego, UNO), estadoDeJuego)

    # Verifica que el tablero del jugador DOS sea válido y cumpla con los requerimientos para tal.
    tableroDeJugadorDOSEsValido: bool = tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego, DOS), estadoDeJuego)

    # Verifica que los ataques esten sincronizados entre tableros.
    losAtaquesCoinciden: bool = coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego, UNO), tableroDeJugador(estadoDeJuego, DOS))

    return hayEntre1y26Filas and hayAlMenosUnaColumna and soloUnJugadorALaVez and hayAlMenosUnBarcoEnJuego and tableroDeJugadorUNOEsValido and tableroDeJugadorDOSEsValido and losAtaquesCoinciden

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

tableroJ2 = ([
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

verificarEj3 = esEstadoDeJuegoVálido(((4,4), [2,2], [DOS], tableroJ1, tableroJ2))
print(verificarEj3)


## Ejercicio 4
# FUNCION PRINCIPAL
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


class DispararEnPosición_Test(unittest.TestCase):
    def test_disparo_en_posicion_vacia(self):
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        
        estado_esperado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_uno_tocado(self):
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[BARCO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        estado_esperado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[BARCO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        resultado = dispararEnPosición(estado, ("A", 1))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_uno_vacia(self):
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        estado_esperado = ((5,5), [3, 2], [DOS],
            ([[BARCO, AGUA, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        resultado = dispararEnPosición(estado, ("A", 2))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_dos_tocado(self):
        estado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        estado_esperado = ((5,5), [3, 2], [UNO],
            ([[BARCO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[BARCO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        resultado = dispararEnPosición(estado, ("A", 2))
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_dos_vacia(self):
        estado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, BARCO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        estado_esperado = ((5,5), [3, 2], [UNO],
            ([[BARCO, AGUA, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[AGUA, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        resultado = dispararEnPosición(estado, ("A", 2))
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)
