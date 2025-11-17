import unittest
from batallaNaval import *

# Tests
# # Tests Ejercicio 1
class cantidadDeBarcosDeTamaño_Test(unittest.TestCase):
    def test_longitud_2_hay_uno_en_el_medio(self): # Un ejemplo de test
        barcos = [[('H',3), ('H',4), ('H',5)],
                  [('F',4), ('E',4)],
                  [('B',4), ('B',3), ('B',2)]]
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2), 1)
        self.assertEqual(barcos, [[('H',3), ('H',4), ('H',5)],
                                  [('F',4), ('E',4)],
                                  [('B',4), ('B',3), ('B',2)]] )
        
    def test_longitud_0(self):
        # En un tablero sin celdas.
        barcos = [[()]]
        # Verifica que la cantidad de barcos de un tablero vacío sea igual a cero.
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2), 0)
        self.assertEqual(barcos, [[()]])

    def test_hay_un_solo_barco(self):
        # En un tablero con una sola celda, y dicha celda resulta ser un barco.
        barcos = [[('E',3)]]
        # Verifica que la cantidad de barcos de este tablero sea igual a uno.
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,1), 1)
        self.assertEqual(barcos, [[('E',3)]])

    def test_longitud_3_no_hay(self):
        # En un tablero sin barcos de longitud 3.
        barcos = [[('A',1), ('A',2)],
                  [('C',1), ('C',2)],
                  [('F',3)]]
        # Verifica que la cantidad de barcos de longitud 3 de este tablero sea igual a cero.
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,3), 0)
        self.assertEqual(barcos, [[('A',1), ('A',2)],
                                  [('C',1), ('C',2)],
                                  [('F',3)]])

# Tests Ejercicio 2
class nuevoJuego_Test(unittest.TestCase):
    def test_2x2_y_un_barco_longitud_2(self):
        grillaUNO_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]

        grillaUNO_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]

        grillaDOS_local = [[VACÍO, VACÍO],
                           [VACÍO, VACÍO]]

        grillaDOS_oponente = [[VACÍO, VACÍO],
                              [VACÍO, VACÍO]]

        juego = nuevoJuego(2,2,[2])

        self.assertEqual(juego[0], (2,2))
        self.assertTrue(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))

    def test_1x1_y_un_barco_longitud_2(self):
        # En un tablero de longitud 3x4.
        grillaUNO_local = [[VACÍO]]

        grillaUNO_oponente = [[VACÍO]]

        grillaDOS_local = [[VACÍO]]

        grillaDOS_oponente = [[VACÍO]]

        juego =nuevoJuego(1, 1, [1])

        # Verifica que el nuevo juego tenga tableros de dimension 1x1.
        self.assertEqual(juego[0], (1,1))
        # Verifica que haya solamente un barco de longitud 2 en el tablero.
        #(Para probar ambiguedad en el enunciado).
        self.assertTrue(juego[1], [2])
        # Verifica que sea el juego inicie con el turno del jugador UNO.
        self.assertEqual(juego[2], [UNO])
        # Verifica el tablero del jugador UNO.
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        # Verifica el tablero del jugador DOS.
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))

    def test_3x4_y_tres_barcos_longitudes_distintas(self):
        # En un tablero de longitud 3x4.
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        juego = nuevoJuego(3, 4, [1, 2, 3])

        # Verifica que el nuevo tablero tenga dimension 3x4.
        self.assertEqual(juego[0], (3, 4))
        # Verifica que en el tablero hayan 3 barcos, uno de longitud
        # 1, otro de longitud 2 y otro de longitud 3.
        self.assertEqual(juego[1], [1, 2, 3])
        # Verifica que sea el juego inicie con el turno del jugador UNO.
        self.assertEqual(juego[2], [UNO])
        # Verifica el tablero del jugador UNO.
        self.assertEqual(juego[3], (grillaUnoLocal, grillaUnoOponente))
        # Verifica el tablero del jugador DOS.
        self.assertEqual(juego[4], (grillaDosLocal, grillaDosOponente))


# Tests Ejercicio 3
class esEstadoDeJuegoVálido_Test(unittest.TestCase):
    # la grillaDOSlocal tiene un solo barco de tamaño 3, en lugar de dos de tamaño 2.
    def test_grilla_DOS_local_no_coincide_con_disponibles(self):
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, BARCO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, BARCO, BARCO, BARCO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        estado = ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [2,2], [DOS], (grillaUnoLocal, grillaUnoOponente), (grillaDosLocal, grillaDosOponente)))


    def test_posiciones_no_coinciden_en_tablero1_vs_tableroOponente0(self):
        # En tablero UNO hay un BARCO que no está reflejado igual en tableroOponente0.
        grillaUnoLocal = [[BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [DOS], (tablero), (tableroOponente))

        # Verifica que el estado de juego NO sea válido.
        self.assertFalse(esEstadoDeJuegoVálido(estado))
        # Verifica que el estado cuente con todas las características que propuse.
        self.assertEqual(estado, ((4,4), [1], [DOS], (tablero), (tableroOponente)))


    def test_posiciones_no_coinciden_en_tableroOponente1_vs_tablero0(self):
        # En tablero DOS oponente hay un BARCO que no está reflejado igual en tablero UNO.
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [DOS], (tablero), (tableroOponente))
        
        # Verifica que el estado de juego NO sea válido.
        self.assertFalse(esEstadoDeJuegoVálido(estado))
        # Verifica que el estado cuente con todas las características que propuse.
        self.assertEqual(estado, ((4,4), [1], [DOS], (tablero), (tableroOponente)))

    def test_n1_menor_que_n2(self):
        # En ambos tablero hay una diferencia de al menos 2 turnos jugados  → debe fallar
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[BARCO, BARCO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))

        # Verifica que el estado de juego NO sea válido.
        self.assertFalse(esEstadoDeJuegoVálido(estado))
        # Verifica que el estado cuente con todas las características que propuse.
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_primero_celda_vacia_con_agua_en_tablero_oponente(self):
        # Caso: celda_tablero == VACÍO pero celda_tableroOponente_op == AGUA → debe fallar
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, AGUA,  VACÍO, VACÍO],  # celda indebida en tablero del oponente
                             [VACÍO, VACÍO, VACÍO, VACÍO]]
        
        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))

        # Verifica que el estado de juego NO sea válido.
        self.assertFalse(esEstadoDeJuegoVálido(estado))
        # Verifica que el estado cuente con todas las características que propuse.
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_segundo_celda_vacia_con_agua_en_tablero_oponente(self):
        # Caso: celda_tablero == VACÍO pero celda_tableroOponente_op == AGUA → debe fallar
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, AGUA, VACÍO, VACÍO],  # celda indebida en tablero del oponente
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))

        # Verifica que el estado de juego NO sea válido.
        self.assertFalse(esEstadoDeJuegoVálido(estado))
        # Verifica que el estado cuente con todas las características que propuse.
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_todo_agua(self):
        # Caso: celda_tablero == AGUA para ambos tableros
        #(o sea que no haya barcos disponibles en el estado de juego) → debe fallar
        grillaUnoLocal = [[AGUA, AGUA, AGUA, AGUA],
                          [AGUA, AGUA, AGUA, AGUA],
                          [AGUA, AGUA, AGUA, AGUA],
                          [AGUA, AGUA, AGUA, AGUA]]

        grillaUnoOponente = [[AGUA, AGUA, AGUA, AGUA],
                             [AGUA, AGUA, AGUA, AGUA],
                             [AGUA, AGUA, AGUA, AGUA],
                             [AGUA, AGUA, AGUA, AGUA]]

        grillaDosLocal = [[AGUA, AGUA, AGUA, AGUA],
                          [AGUA, AGUA, AGUA, AGUA],
                          [AGUA, AGUA, AGUA, AGUA],
                          [AGUA, AGUA, AGUA, AGUA]]

        grillaDosOponente = [[AGUA, AGUA, AGUA, AGUA],
                             [AGUA, AGUA, AGUA, AGUA],
                             [AGUA, AGUA, AGUA, AGUA],
                             [AGUA, AGUA, AGUA, AGUA]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [DOS], (tablero), (tableroOponente))

        # Verifica que el estado de juego NO sea válido.
        self.assertFalse(esEstadoDeJuegoVálido(estado))
        # Verifica que el estado cuente con todas las características que propuse.
        self.assertEqual(estado, ((4,4), [1], [DOS], (tablero), (tableroOponente)))


    def test_todo_vacío(self):
        # Caso: celda_tablero == VACÍO para ambos tableros
        #(o sea que no haya barcos disponibles en el estado de juego) → debe fallar
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))

        # Verifica que el estado de juego NO sea válido.
        self.assertFalse(esEstadoDeJuegoVálido(estado))
        # Verifica que el estado cuente con todas las características que propuse.
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


#Tests Ejercicio 4
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
        # Jugador UNO lanzó un disparo e impactó, por lo que el estado debería cambiar
        #y jugador UNO debería marcar ese barco en su tablero oponente.
        estado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[BARCO, BARCO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, BARCO, BARCO, BARCO],
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
            ([[BARCO, BARCO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, BARCO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        resultado = dispararEnPosición(estado, ("A", 1))
        # Verifica que un barco haya sido impactado.
        self.assertEqual(resultado, TOCADO)
        # Verifica que el estado del tablero antes y despues del disparo no cambien.
        self.assertEqual(estado, estado_esperado)


    def test_disparo_en_posicion_dos_tocado(self):
        # Jugador UNO lanzó un disparo e impactó, por lo que el estado debería cambiar
        #y jugador UNO debería marcar ese barco en su tablero oponente.
        estado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )

        estado_esperado = ((5,5), [3, 2], [UNO],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
            [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
            [[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
             [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])
        )
        resultado = dispararEnPosición(estado, ("A", 1))
        # Verifica que un barco haya sido impactado.
        self.assertEqual(resultado, TOCADO)
        # Verifica que el estado del tablero antes y despues del disparo no cambien.
        self.assertEqual(estado, estado_esperado)


    def test_disparo_en_posicion_dos_vacia(self):
        # Jugador DOS lanzó un disparo y NO impactó, por lo que el estado debería cambiar
        #y jugador DOS debería marcar ese espacio como AGUA en su tablero oponente.
        estado = ((5,5), [3, 2], [DOS],
            ([[BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        estado_esperado = ((5,5), [3, 2], [UNO],
            ([[BARCO, AGUA, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [BARCO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, BARCO, BARCO]],
             [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]),
            ([[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [BARCO, BARCO, BARCO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, BARCO, BARCO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]],
             [[VACÍO, AGUA, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
              [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]))

        resultado = dispararEnPosición(estado, ("A", 2))
        # Verifica que ningún barco haya sido impactado.
        self.assertEqual(resultado, NADA)
        # Verifica que el estado del tablero antes y despues del disparo no cambien.
        self.assertEqual(estado, estado_esperado)


#Tests Ejercicio 5
class barcosEnGrilla_Test(unittest.TestCase):
    def test_varios_barcos_distintos_tamanios(self):
        # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]

        barcosEsperados: list[BarcoEnGrilla] = [[('D',3), ('D',4)],
                                                [('B',6), ('B',5), ('B',4)],
                                                [('D',6), ('E',6)],
                                                [('D',1),('C',1), ('B',1)]]

        # Pensar! qué pasa si el orden de los barcos en la lista no es el mismo? respeta la especificación?
        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, BARCO, BARCO, VACÍO, BARCO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]])


    def test_descarto_barco_invalido_con_celda_agua(self):
        grilla: Grilla = [[BARCO, BARCO, AGUA, VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, BARCO, BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]

        barcosEsperados: list[BarcoEnGrilla] = [[("C",1),("C",2),("C",3)]]

        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[BARCO, BARCO, AGUA, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, BARCO, BARCO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])


    def test_varios_barcos_uno_de_tamanio_uno(self):
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                          [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO, VACÍO, BARCO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]]

        barcosEsperados: list[BarcoEnGrilla] = [[('D',3)],
                                                [('B',6), ('B',5), ('B',4)],
                                                [('D',6), ('E',6)],
                                                [('D',1),('C',1), ('B',1)]]

        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, BARCO, BARCO, BARCO, VACÍO],
                                  [BARCO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [BARCO, VACÍO, BARCO, VACÍO, VACÍO, BARCO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, BARCO, VACÍO]])


    def test_un_solo_barco(self):
        grilla: Grilla = [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]]

        barcosEsperados: list[BarcoEnGrilla] = [[('B',4)]]

        self.assertTrue(barcosEnGrilla(grilla), barcosEsperados)
        self.assertEqual(grilla, [[VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, BARCO, VACÍO, VACÍO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO],
                                  [VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO, VACÍO]])


# Tests Ejercicio 6
class elJugadorConMejorPuntería_Test(unittest.TestCase):
    def test_gana_jugador_dos(self):
        # En tablero DOS oponente hay mas celdas BARCO que en
        #tablero UNO oponente, tal que estas celdas no sean adyacentes.
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [AGUA, VACÍO, BARCO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, AGUA, BARCO],
                             [VACÍO, AGUA, VACÍO, BARCO],
                             [VACÍO, VACÍO, VACÍO, AGUA],
                             [AGUA, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, AGUA, BARCO],
                          [VACÍO, AGUA, VACÍO, BARCO],
                          [VACÍO, BARCO, BARCO, AGUA],
                          [AGUA, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, AGUA, AGUA, VACÍO],
                             [BARCO, VACÍO, BARCO, AGUA],
                             [AGUA, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))
        
        # Verifica que el jugador con mejor puntería es el jugador DOS.
        self.assertEqual(elJugadorConMejorPuntería(estado), DOS)


    def test_gana_jugador_uno(self):
        # En tablero UNO oponente hay mas celdas BARCO que en
        #tablero DOS oponente, tal que estas celdas no sean adyacentes.
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [BARCO, AGUA, AGUA, VACÍO],
                          [BARCO, VACÍO, BARCO, VACÍO],
                          [AGUA, VACÍO, BARCO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, AGUA, BARCO],
                             [VACÍO, AGUA, VACÍO, VACÍO],
                             [VACÍO, BARCO, VACÍO, AGUA],
                             [AGUA, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, AGUA, BARCO],
                          [VACÍO, AGUA, VACÍO, BARCO],
                          [VACÍO, BARCO, BARCO, AGUA],
                          [AGUA, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [BARCO, AGUA, AGUA, VACÍO],
                             [BARCO, VACÍO, VACÍO, AGUA],
                             [AGUA, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))
        
        # Verifica que el jugador con mejor puntería es el jugador UNO.
        self.assertEqual(elJugadorConMejorPuntería(estado), UNO)

if __name__ == '__main__':
    unittest.main(verbosity=1)

