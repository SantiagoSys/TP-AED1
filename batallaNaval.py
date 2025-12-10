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
    grilla_local: Grilla = crearGrillaVacia(cantidadDeFilas, cantidadDeColumnas)
    grilla_oponente: Grilla = crearGrillaVacia(cantidadDeFilas, cantidadDeColumnas)
    return (grilla_local, grilla_oponente)

def crearGrillaVacia(cantidadDeFilas: int, cantidadDeColumnas: int) -> Grilla:
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
    tablero: Tablero = estadoDeJuego[3]
    tableroOponente: Tablero = estadoDeJuego[4]

    if len(tablero) != 2 or len(tableroOponente) != 2:
        return False

    hayEntre1y26Filas: bool = cantidadDeFilasEstadoJuego(estadoDeJuego) >= 1 and cantidadDeFilasEstadoJuego(estadoDeJuego) <= 26

    hayAlMenosUnaColumna: bool = cantidadDeColumnasEstadoJuego(estadoDeJuego) > 0

    soloUnJugadorALaVez: bool = len(estadoDeJuego[2]) == 1

    hayAlMenosUnBarcoEnJuego: bool = len(barcosDisponibles(estadoDeJuego)) > 0

    tableroDeJugadorUNOEsValido: bool = tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego, UNO), estadoDeJuego)

    tableroDeJugadorDOSEsValido: bool = tableroVálidoEnJuego(tableroDeJugador(estadoDeJuego, DOS), estadoDeJuego)

    losAtaquesCoinciden: bool = False
    if tableroDeJugadorUNOEsValido and tableroDeJugadorDOSEsValido:
        losAtaquesCoinciden: bool = coincidenPosicionesAtacadas(tableroDeJugador(estadoDeJuego, UNO), tableroDeJugador(estadoDeJuego, DOS))

    return hayEntre1y26Filas and hayAlMenosUnaColumna and soloUnJugadorALaVez and hayAlMenosUnBarcoEnJuego and tableroDeJugadorUNOEsValido and tableroDeJugadorDOSEsValido and losAtaquesCoinciden

    
# FUNCIONES AUXILIARES
def coincidenPosicionesAtacadas(tablero: Tablero, tableroOponente: Tablero) -> bool:
    grilla_uno_local: Grilla = tablero[0]
    grilla_uno_oponente: Grilla = tablero[1]
    grilla_dos_local: Grilla = tableroOponente[0]
    grilla_dos_oponente: Grilla = tableroOponente[1]
    
    n1: int = 0     # Celdas no vacías en tablero1
    n2: int = 0     # Celdas no vacías en tableroOponente1
    
    filas: int = len(grilla_uno_local)
    columnas: int = len(grilla_uno_local[0])
    
    for i in range(filas):
        for j in range(columnas):

            celda_tablero: Celda = grilla_uno_local[i][j]
            celda_tablero_op: Celda = grilla_uno_oponente[i][j]

            celda_tableroOponente: Celda = grilla_dos_local[i][j]
            celda_tableroOponente_op: Celda = grilla_dos_oponente[i][j]
            
            if celda_tablero_op != VACÍO:
                n1 += 1
            if celda_tableroOponente_op != VACÍO:
                n2 += 1

            if not coincidenTablero1Oponente0(celda_tablero_op, celda_tableroOponente):
                return False
            
            if not coincidenOponente1Tablero0(celda_tableroOponente_op, celda_tablero):
                return False
            
    return 0 <= n1 - n2 <= 1


def coincidenTablero1Oponente0(celda_tablero_op: Celda, celda_tableroOponente: Celda) -> bool:
    if celda_tablero_op != VACÍO:
        return celda_tableroOponente == celda_tablero_op
    else:
        return celda_tableroOponente == VACÍO or celda_tableroOponente == BARCO


def coincidenOponente1Tablero0(celda_tableroOponente_op: Celda, celda_tablero: Celda) -> bool:
    if celda_tableroOponente_op != VACÍO:
        return celda_tablero == celda_tableroOponente_op
    else:
        return celda_tablero == VACÍO or celda_tablero == BARCO


def mismosElementos(lista1: list[Any], lista2: list[Any]) -> bool:
    lasDosIguales: bool = True

    for elemento in lista1:
        if cantidadDeApariciones(elemento, lista1) != cantidadDeApariciones(elemento, lista2):
            lasDosIguales = False
    for elemento in lista2:
        if cantidadDeApariciones(elemento, lista1) != cantidadDeApariciones(elemento, lista2):
            lasDosIguales = False
            
    return lasDosIguales


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

    tablero_jugador_actual: Tablero = tableroDeJugador(estado_juego, jugador_actual)
    tablero_jugador_oponente: Tablero = tableroDeJugador(estado_juego, jugador_oponente)

    grilla_oponente_jugador_actual: Grilla = grillaOponente(tablero_jugador_actual)
    grilla_local_jugador_oponente: Grilla = grillaLocal(tablero_jugador_oponente)

    celda_objetivo: Celda = celdaEnPosición(grilla_local_jugador_oponente, posición)
    if celda_objetivo == BARCO:
        cambiarCeldaGrilla(grilla_oponente_jugador_actual, posición, BARCO)
        resultado: ResultadoDisparo = TOCADO
    else:
        cambiarCeldaGrilla(grilla_oponente_jugador_actual, posición, AGUA)
        cambiarCeldaGrilla(grilla_local_jugador_oponente, posición, AGUA)
        resultado: ResultadoDisparo = NADA

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

    letras: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']  # Crea una lista de str de las letras que tengo permitido utilizar según el enunciado.

    for i in range(filas):
        for j in range(columnas):
            posición: Posición = (letras[i], j+1)
            
            if grilla[i][j] != VACÍO and not algúnBarcoOcupaLaPosición(res, posición):
                barco: BarcoEnGrilla = descubrirBarcoEnPosición(grilla, i, j, letras)
                
                if posicionesOcupadasEnGrilla(grilla, barco):
                    res.append(barco)

    if not sonBarcosVálidos(res):
        return []
    
    return res


# FUNCIONES AUXILIARES
def descubrirBarcoEnPosición(grilla: Grilla, fila: int, col: int, letras: list[str]) -> BarcoEnGrilla:
    posición: Posición = (letras[fila], col + 1)

    if sePuedeConstruirBarcoHorizontalDesde(grilla, posición):
        return descubrirBarcoHorizontal(grilla, fila, col, letras)

    elif sePuedeConstruirBarcoVerticalDesde(grilla, posición):
        return descubrirBarcoVertical(grilla, fila, col, letras)

    else:
        return [posición]

def descubrirBarcoHorizontal(grilla: Grilla, fila: int, col: int, letras: list[str]) -> BarcoEnGrilla:
    barco: BarcoEnGrilla = []
    columnas: int = len(grilla[0])
    
    k: int = col
    while k < columnas and grilla[fila][k] == BARCO:
        barco.append((letras[fila], k + 1))
        k += 1
    
    return barco

def descubrirBarcoVertical(grilla: Grilla, fila: int, col: int, letras: list[str]) -> BarcoEnGrilla:
    barco: BarcoEnGrilla = []
    filas: int = len(grilla)
    
    k: int = fila
    while k < filas and grilla[k][col] == BARCO:
        barco.append((letras[k], col + 1))
        k += 1

    return barco

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


## Ejercicio 6
# FUNCION PRINCIPAL
def elJugadorConMejorPuntería(estadoDeJuego: EstadoJuego) -> Jugador:
    """
    Indica el jugador con mejor puntería del estado actual del juego 'estadoDeJuego'.
    
    PRE: esEstadoDeJuegoVálido(estadoDeJuego)
         punteríaDeJugador(estadoDeJuego, UNO) ̸= punteríaDeJugador(estadoDeJuego, DOS)
         
    Args:
        estadoDeJuego (EstadoJuego): tuple[Dimensiones, list[Barco], list[Jugador], Tablero, Tablero] que indica el estado actual del juego.
    
    Returns:
        UNO si punteríaDeJugador(estadoDeJuego, UNO) es mayor que punteríaDeJugador(estadoDeJuego, DOS), DOS si es menor.
    """
    if punteríaDeJugador(estadoDeJuego, UNO) > punteríaDeJugador(estadoDeJuego, DOS):
        return UNO
    else:
        return DOS


# FUNCIONES AUXILIARES
def punteríaDeJugador(estadoDeJuego: EstadoJuego, jugador: Jugador) -> int:
    res: int = cantidadDeBarcosDescubiertos(estadoDeJuego, jugador) - cantidadDePosicionesConAgua(grillaOponente(tableroDeJugador(estadoDeJuego, jugador)))

    return res


def cantidadDeBarcosDescubiertos(estadoDeJuego: EstadoJuego, jugador: Jugador) -> int:
    res: int = 0

    oponente: Jugador = jugadorOpuesto(jugador)

    barcos_oponente: list[BarcoEnGrilla] = barcosEnGrilla(grillaLocal(tableroDeJugador(estadoDeJuego, oponente)))

    for barco in barcos_oponente:
        if barcoDescubiertoEn(barco, grillaOponente(tableroDeJugador(estadoDeJuego, jugador))):
            res += 1
    
    return res


def cantidadDePosicionesConAgua(grilla: Grilla) -> int:
    res: int = 0
    letras: list[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    filas: int = len(grilla)
    columnas: int = len(grilla[0])

    for i in range(filas):
        for j in range(columnas):
            posición: Posición = (letras[i], j+1)
            if esAgua(posición, grilla):
                res += 1
    
    return res


def barcoDescubiertoEn(barco: BarcoEnGrilla, grilla: Grilla) -> bool:
    for posición in barco:
        if celdaEnPosición(grilla, posición) != VACÍO:
            return True
    
    return False


def jugadorOpuesto(jugador: Jugador) -> Jugador:
    if jugador == UNO:
        return DOS
    else:
        return UNO


def esAgua(posición: Posición, grilla: Grilla) -> bool:
    if celdaEnPosición(grilla, posición) == AGUA:
        return True
    return False


def juegoTerminado(estadoDeJuego: EstadoJuego) -> bool:
    return todosLosBarcosHundidos(estadoDeJuego, UNO) or todosLosBarcosHundidos(estadoDeJuego, DOS)

def todosLosBarcosHundidos(estadoDeJuego: EstadoJuego, jugador: Jugador) -> bool:
    tablero_jugador: Tablero = tableroDeJugador(estadoDeJuego, jugador)

    # Esta es la grilla correcta: los disparos del rival hacia "jugador"
    grilla_disparos_rival: Grilla = grillaOponente(tableroDeJugador(estadoDeJuego, jugadorOpuesto(jugador)))

    for barco in barcosEnGrilla(grillaLocal(tablero_jugador)):
        if not barcoHundidoEn(barco, grilla_disparos_rival):
            return False

    return True

def barcoHundidoEn(barco: BarcoEnGrilla, grilla: Grilla) -> bool:
    for posición in barco:
        if celdaEnPosición(grilla, posición) != BARCO:
            return False
    return True

def jugadorGanador(estadoDeJuego: EstadoJuego) -> Jugador:
    if juegoTerminado(estadoDeJuego):
        return turno(estadoDeJuego)



# ejemplo = elJugadorConMejorPunter´ıa(((4,4),⟨2,2⟩,⟨UNO⟩,(⟨
#  ⟨V ACIO,VACIO,VACIO,VACIO⟩,
#  ⟨BARCO,AGUA,AGUA,VACIO⟩,
#  ⟨BARCO,VACIO,BARCO,AGUA⟩,
#  ⟨AGUA,VACIO,BARCO,VACIO⟩
#  ⟩,⟨
#  ⟨V ACIO,VACIO,AGUA,BARCO⟩,
#  ⟨V ACIO,AGUA,VACIO,BARCO⟩,
#  ⟨V ACIO,VACIO,VACIO,AGUA⟩,
#  ⟨AGUA,VACIO,VACIO,VACIO⟩
#  ⟩),(⟨
#  ⟨V ACIO,VACIO,AGUA,BARCO⟩,
#  ⟨V ACIO,AGUA,VACIO,BARCO⟩,
#  ⟨V ACIO,BARCO,BARCO,AGUA⟩,
#  ⟨AGUA,VACIO,VACIO,VACIO⟩
#  ⟩,⟨
#  ⟨V ACIO,VACIO,VACIO,VACIO⟩,
#  ⟨V ACIO,AGUA,AGUA,VACIO⟩,
#  ⟨BARCO,VACIO,BARCO,AGUA⟩,
#  ⟨AGUA,VACIO,VACIO,VACIO⟩
#  ⟩)))


def cantidadDeBarcosHundidos(estadoDeJuego: EstadoJuego, jugador: Jugador) -> int:
    # Determino el oponente
    jugadores: list[Jugador] = estadoDeJuego[2]
    jugadorOpuesto: Jugador = UNO
    for j in jugadores:
        if j != jugador:
            jugadorOpuesto = j

    # Obtengo tableros
    tableroActual = tableroDeJugador(estadoDeJuego, jugador)
    tableroEnemigo = tableroDeJugador(estadoDeJuego, jugadorOpuesto)

    grillaAtaques: Grilla = grillaOponente(tableroActual)
    barcosDelEnemigo: list[BarcoEnGrilla] = tableroEnemigo[0]  # grillaLocal? o lista de barcos, depende del modelo

    # Contador
    cant: int = 0

    # Recorro cada barco
    for barco in barcosDelEnemigo:
        hundido: bool = True

        # Verifico si todas las posiciones fueron tocadas
        for pos in barco:
            letra: str = pos[0]
            numero: int = pos[1]
            if celdaEnPosición(grillaAtaques, (letra, numero)) != BARCO:
                hundido = False

        if hundido:
            cant = cant + 1

    return cant


def barcoMásCercanoASerHundido(estadoDeJuego: EstadoJuego, jugador: Jugador) -> BarcoEnGrilla:
    dimensiones: Dimensiones = estadoDeJuego[0]
    barcosDisponibles: list[Barco] = estadoDeJuego[1]
    turnos: list[Jugador] = estadoDeJuego[2]
    tablerosLocales: Tablero = estadoDeJuego[3]
    tablerosOponentes: Tablero = estadoDeJuego[4]

    # Determinar jugador oponente
    jugadorOpuesto: Jugador = UNO
    if jugador == UNO:
        jugadorOpuesto = DOS
    else:
        jugadorOpuesto = UNO

    # Seleccionar grilla local + grilla donde se registran los disparos
    grillaLocalOponente: Grilla = tablerosLocales[jugadorOpuesto == DOS]
    grillaDisparosDelJugador: Grilla = tablerosOponentes[jugador == DOS]

    # Obtener todos los barcos en la grilla del oponente
    barcosEnemigos: list[BarcoEnGrilla] = barcosEnGrilla(grillaLocalOponente)

    mejorBarco: BarcoEnGrilla = []
    maxTocadas: int = -1

    # Buscar el barco con mayor cantidad de posiciones tocadas
    for barco in barcosEnemigos:
        tocadas: int = 0
        for pos in barco:
            # Si la celda en la grilla de disparos del jugador es TOCADO
            if celdaEnPosición(grillaDisparosDelJugador, pos) == TOCADO:
                tocadas = tocadas + 1

        # Es el más cercano a hundirse si tiene más tocadas
        if tocadas > maxTocadas:
            maxTocadas = tocadas
            mejorBarco = barco.copy()  # copia permitida

    return mejorBarco


def quedanBarcosSinTocar(estadoDeJuego: EstadoJuego, jugador: Jugador) -> bool:
    # Extraemos las grillas relevantes
    tablero_jugador: Tablero = tableroDeJugador(estadoDeJuego, jugador)
    grilla_barcos: Grilla = grillaLocal(tablero_jugador)

    # Obtenemos todos los barcos del jugador en forma de lista de BarcoEnGrilla
    barcos: list[BarcoEnGrilla] = barcosEnGrilla(grilla_barcos)

    # Recorremos cada barco y verificamos si tiene al menos una posición sin tocar
    for barco in barcos:
        # Para cada posición del barco verificamos si sigue siendo BARCO en la grilla
        for posicion in barco:
            if celdaEnPosición(grilla_barcos, posicion) == BARCO:
                # Todavía queda una parte del barco intacta → quedan barcos sin tocar
                return True

    # Si recorrimos todo y nunca vimos un BARCO intacto, no quedan barcos sin tocar
    return False


def esBarcoHundido(grillaOponente: Grilla, barco: BarcoEnGrilla) -> bool:
    """
    Devuelve True si todas las posiciones del barco han sido atacadas
    en la grillaOponente.
    """
    # Recorremos cada posición del barco:
    for pos in barco:
        # Si alguna posición NO está atacada (no es AGUA), entonces no está hundido
        if celdaEnPosición(grillaOponente, pos) != AGUA:
            return False

    # Si todas las posiciones estaban atacadas
    return True
