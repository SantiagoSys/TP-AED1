from typing import Any
from biblioteca import *

## Ejercicio 1
# FUNCION PRINCIPAL
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


## Ejercicio 2
# FUNCION PRINCIPAL
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
        Un nuevo estado de juego 'EstadoJuego', donde ambos tableros 'Tablero' en 'EstadoJuego' comienzan vacíos.
    """
    return ((cantidadDeFilas, cantidadDeColumnas), barcosDisponibles, [UNO], nuevoTablero(cantidadDeFilas, cantidadDeColumnas), nuevoTablero(cantidadDeFilas, cantidadDeColumnas))


# FUNCIONES AUXILIARES
def nuevoTablero(cantidadDeFilas: int, cantidadDeColumnas: int) -> Tablero:
    grilla_local: Grilla = nuevoTableroAux(cantidadDeFilas, cantidadDeColumnas)
    grilla_oponente: Grilla = nuevoTableroAux(cantidadDeFilas, cantidadDeColumnas)
    return (grilla_local, grilla_oponente)

def nuevoTableroAux(cantidadDeFilas: int, cantidadDeColumnas: int) -> Grilla:
    grilla: Grilla = []
    for i in range(0, cantidadDeFilas):
        fila_con_vacios: list[Celda] = []
        for j in range(0, cantidadDeColumnas):
            fila_con_vacios.append(VACÍO)
        grilla.append(fila_con_vacios)
    return grilla


## Ejercicio 3
# FUNCION PRINCIPAL
def esEstadoDeJuegoVálido(estadoDeJuego: EstadoJuego) -> bool:
    """
    Indica si el estado de juego 'estadoDeJuego' es válido.
    
    PRE: True
    
    Args:
        estadoDeJuego (EstadoJuego): tuple[Dimensiones, list[Barco], list[Jugador], Tablero, Tablero] que indica el estado actual del juego.
    
    Returns:
        True si es un estado de juego válido, False si no.
    """
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
    
# FUNCIONES AUXILIARES
def coincidenPosicionesAtacadas(tablero: Tablero, tableroOponente: Tablero) -> bool:
    grilla_uno_local = tablero[0]
    grilla_dos_local = tableroOponente[0]
    grilla_uno_oponente = tablero[1]
    grilla_dos_oponente = tableroOponente[1]
    
    n1 = 0  # Celdas no vacías en tablero1
    n2 = 0  # Celdas no vacías en tableroOponente1
    
    filas = len(grilla_uno_local)
    columnas = len(grilla_uno_local[0])
    
    for i in range(filas):
        for j in range(columnas):
            celda_tablero = grilla_uno_local[i][j]
            celda_tablero_op = grilla_dos_local[i][j]
            celda_tableroOponente = grilla_uno_oponente[i][j]
            celda_tableroOponente_op = grilla_dos_oponente[i][j]
            
            if celda_tablero != VACÍO:
                n1 += 1
            if celda_tableroOponente != VACÍO:
                n2 += 1

            # --- Primera parte del asegura ---
            # tablero1 -> tableroOponente0
            if celda_tablero != VACÍO:
                if celda_tableroOponente_op != celda_tablero:
                    return False
            else:
                if not (celda_tableroOponente_op == VACÍO or celda_tableroOponente_op == BARCO):
                    return False

            # --- Segunda parte del asegura ---
            # tableroOponente1 -> tablero0
            if celda_tableroOponente != VACÍO:
                if celda_tablero_op != celda_tableroOponente:
                    return False
            else:
                if not (celda_tablero_op == VACÍO or celda_tablero_op == BARCO):
                    return False
            
    
    if n1 - n2 < 0 or n1 - n2 > 1:
        return False

    return True

def mismosElementos(lista1: list[Any], lista2: list[Any]) -> bool:
    # Indica si cada uno de los elementos pertenecientes a la primera lista aparece también en la segunda.
    for elemento in lista1:
        if cantidadDeApariciones(elemento, lista1) != cantidadDeApariciones(elemento, lista2):  # cantidadDeApariciones me devuelve la cantidad de veces
            return False                                                                       # que un elemento aparece en una lista.
    return True

def tamaños(barcos: list[BarcoEnGrilla]) -> list[int]:
    # Devuelve el tamaño de cada uno de los barcos en la grilla.
    res: list[int] = []

    for barco in barcos:
        tamaño: int = len(barco)
        res.append(tamaño)  

    return res

def coincidenBarcosEnGrilla(barcos: list[Barco], grilla: Grilla) -> bool:
    # Indica si los barcos pertenecientes a la grilla coinciden con los tamaños esperados.
    return mismosElementos(barcos, tamaños(barcosEnGrilla(grilla)))

def tableroVálidoEnJuego(tablero: Tablero, estadoDeJuego: EstadoJuego) -> bool:
    # Indica si tanto la grilla local como la del oponente son válidas y si los barcos en la grilla local coinciden con los tamaños esperados.
    res: bool = grillaVálidaEnJuego(grillaLocal(tablero), estadoDeJuego) and grillaVálidaEnJuego(grillaOponente(tablero), estadoDeJuego) and coincidenBarcosEnGrilla(barcosDisponibles(estadoDeJuego), grillaLocal(tablero))
    return res


## Ejercicio 4
# FUNCION PRINCIPAL
def dispararEnPosición(estado_juego: EstadoJuego, posición: Posición) -> ResultadoDisparo:
    """
    Dispara en la posición 'posición', modificando el estado de juego 'estado_juego' si es que se impactó o no un barco
    y cambiando el turno del jugador.
    
    PRE: esEstadoDeJuegoVálido(estadoDeJuego)
         esPosiciónVálidaEnGrilla(posición, grillaOponente(tableroDeJugador(estadoDeJuego, turno(estadoDeJuego))))
         celdaEnPosición(grillaOponente(tableroDeJugador(estadoDeJuego, turno(estadoDeJuego))), posición) = VACÍO
    
    Args:
        estado_juego (EstadoJuego): tuple[Dimensiones, list[Barco], list[Jugador], Tablero, Tablero] que indica el estado actual del juego.
        posición (Posición): Tupla(str, int) que indica la posición del disparo.
    
    Modifica:
        estadoDeJuego
        
    Returns:
        TOCADO si el disparo impactó un barco y NADA si no.
    """
    jugador_actual: Jugador = turno(estado_juego)
    if jugador_actual == UNO:
        jugador_oponente: Jugador = DOS
    else:
        jugador_oponente: Jugador = UNO

    # Obtenemos el tablero de ambos.
    tablero_jugador_actual: Tablero = tableroDeJugador(estado_juego, jugador_actual)
    tablero_jugador_oponente: Tablero = tableroDeJugador(estado_juego, jugador_oponente)

    grilla_oponente_jugador_actual: Grilla = grillaOponente(tablero_jugador_actual)     # Obtenemos la grilla oponente del jugador actual.
    grilla_local_jugador_oponente: Grilla = grillaLocal(tablero_jugador_oponente)       # Obtenemos la grilla local del jugador oponente.

    # Vemos qué hay en la posición objetivo
    celda_objetivo: Celda = celdaEnPosición(grilla_local_jugador_oponente, posición)
    if celda_objetivo == BARCO:
        cambiarCeldaGrilla(grilla_oponente_jugador_actual, posición, BARCO)
        resultado: ResultadoDisparo = TOCADO
    else:
        cambiarCeldaGrilla(grilla_oponente_jugador_actual, posición, AGUA)
        cambiarCeldaGrilla(grilla_local_jugador_oponente, posición, AGUA)
        resultado: ResultadoDisparo = NADA

    # Cambiamos el turno al otro jugador
    cambiarTurno(estado_juego)

    return resultado


## Ejercicio 5
# FUNCION PRINCIPAL
def barcosEnGrilla(grilla: Grilla) -> list[BarcoEnGrilla]:
    """
    Crea una lista con todos los barcos que hay en la grilla 'grilla'.
    
    PRE: esGrillaVálida(grilla)
         ∀ posición 'posición' de tipo Posición que sea válida en la grilla 'grilla' se cumple: noHayMásDeUnaFormaDeConstruirUnBarcoDesde(grilla, posición)
         
    Args:
        grilla (Grilla): list[list[Celda]] que indica la grilla del juego.
    
    Returns:
        Lista de barcos, donde cada barco es una lista de posiciones que ocupa en la grilla.
    """
    res: list[BarcoEnGrilla] = []
    filas: int = len(grilla)
    columnas: int = len(grilla[0])

    # Crea una lista de str de las letras que tengo permitido utilizar según el enunciado.
    letras: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    for i in range(filas):
        for j in range(columnas):
            posición: Posición = (letras[i], j+1)
            
            # Solamente si la celda es un BARCO y ningún barco ocupa ya esa posición avanzo con
            if grilla[i][j] == BARCO and not algúnBarcoOcupaLaPosición(res, posición):
                barco: BarcoEnGrilla = []

                # Indica si alguna celda adyacente horizontal a la que estoy parado es igual a BARCO.
                if sePuedeConstruirBarcoHorizontalDesde(grilla, posición):
                    k: int = j  # Para que el while no me modifique el j de afuera creo la variable k.
                    while k < columnas and grilla[i][k] == BARCO:
                        barco.append((letras[i], k+1))
                        k += 1
                
                # Indica si alguna celda adyacente vertical a la que estoy parado es igual a BARCO.
                elif sePuedeConstruirBarcoVerticalDesde(grilla, posición):
                    k: int = i  # Para que el while no me modifique el i de afuera creo la variable k.
                    while k < filas and grilla[k][j] == BARCO:
                        barco.append((letras[k], j+1))
                        k += 1
                
                # En caso de que no haya ninguna celda adyacente igual a BARCO, añado a la lista esa única posición.
                else:
                    barco.append(posición)
                
                if posicionesOcupadasEnGrilla(grilla, barco):
                    res.append(barco)

    return res

# FUNCIONES AUXILIARES
def algúnBarcoOcupaLaPosición(barcos: list[BarcoEnGrilla], posición: Posición) -> bool:
    # Indica tal que dada una posición y una lista de posiciones, si dicha posición pertenece a la lista.
    for barco in barcos:
        if posición in barco:
            return True
    return False

def posicionesOcupadasEnGrilla(grilla: Grilla, posiciones: list[Posición]) -> bool:
    for posición in posiciones:
        if celdaEnPosición(grilla, posición) != BARCO:  # celdaEnPosición dada una grilla y una posición, me devuelve
            return False                               # lo que ponía la celda en dicha posición (AGUA, BARCO O VACÍO).
    return True                                         # hayBarcoAl me indica si hay una posición adyacente a *posición* hacia *dirección* en la grilla *grilla* que tenga barco.

def sePuedeConstruirBarcoVerticalDesde(grilla: Grilla, posición: Posición) -> bool:
    # Determina si desde una posición dada se puede construir un barco en orientación vertical.
    return celdaEnPosición(grilla, posición) == BARCO and (hayBarcoAl(grilla, posición, ARRIBA) or hayBarcoAl(grilla, posición, ABAJO))

def sePuedeConstruirBarcoHorizontalDesde(grilla: Grilla, posición: Posición) -> bool:
    # Determina si desde una posición dada se puede construir un barco en orientación horizontal.
    return celdaEnPosición(grilla, posición) == BARCO and (hayBarcoAl(grilla, posición, DERECHA) or hayBarcoAl(grilla, posición, IZQUIERDA))




