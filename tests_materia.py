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
        barcos = [[()]]
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,2), 0)
        self.assertEqual(barcos, [[()]])

    def test_hay_un_solo_barco(self):
        barcos = [[('E',3)]]
        self.assertEqual(cantidadDeBarcosDeTamaño(barcos,1), 1)
        self.assertEqual(barcos, [[('E',3)]])

    def test_longitud_3_no_hay(self):
        barcos = [[('A',1), ('A',2)],
                  [('C',1), ('C',2)],
                  [('F',3)]]
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
        grillaUNO_local = [[VACÍO]]

        grillaUNO_oponente = [[VACÍO]]

        grillaDOS_local = [[VACÍO]]

        grillaDOS_oponente = [[VACÍO]]

        juego =nuevoJuego(1, 1, [1])

        self.assertEqual(juego[0], (1,1))
        self.assertTrue(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUNO_local, grillaUNO_oponente))
        self.assertEqual(juego[4], (grillaDOS_local, grillaDOS_oponente))

    def test_3x4_y_tres_barcos_longitudes_distintas(self):
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

        self.assertEqual(juego[0], (3, 4))
        self.assertEqual(juego[1], [1, 2, 3])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUnoLocal, grillaUnoOponente))
        self.assertEqual(juego[4], (grillaDosLocal, grillaDosOponente))
    
    def test_1x4_un_barco_longitud_2(self):
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO]]

        juego = nuevoJuego(1, 4, [2])

        self.assertEqual(juego[0], (1, 4))
        self.assertEqual(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUnoLocal, grillaUnoOponente))
        self.assertEqual(juego[4], (grillaDosLocal, grillaDosOponente))
    
    def test_4x1_un_barco_longitud_2(self):
        grillaUnoLocal = [[VACÍO],
                          [VACÍO],
                          [VACÍO],
                          [VACÍO]]

        grillaUnoOponente = [[VACÍO],
                             [VACÍO],
                             [VACÍO],
                             [VACÍO]]

        grillaDosLocal = [[VACÍO],
                          [VACÍO],
                          [VACÍO],
                          [VACÍO]]

        grillaDosOponente = [[VACÍO],
                             [VACÍO],
                             [VACÍO],
                             [VACÍO]]
        
        juego = nuevoJuego(4, 1, [2])

        self.assertEqual(juego[0], (4, 1))
        self.assertEqual(juego[1], [2])
        self.assertEqual(juego[2], [UNO])
        self.assertEqual(juego[3], (grillaUnoLocal, grillaUnoOponente))
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

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [DOS], (tablero), (tableroOponente)))


    def test_posiciones_no_coinciden_en_tableroOponente1_vs_tablero0(self):
        # En tablero DOS oponente hay un BARCO que no está reflejado igual en tablero UNO.
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

        grillaDosOponente = [[BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [DOS], (tablero), (tableroOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [DOS], (tablero), (tableroOponente)))


    def test_n1_menor_que_n2(self):
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

        self.assertFalse(esEstadoDeJuegoVálido(estado))
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

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_segundo_celda_vacia_con_agua_en_tablero_oponente(self):
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

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_todo_agua(self):
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

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [DOS], (tablero), (tableroOponente)))


    def test_todo_vacío(self):
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

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_alguna_grilla_vacía(self):
        grillaUnoLocal = []

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

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_grillas_con_distintas_dimensiones(self):
        grillaUnoLocal = [[VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO],
                             [VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO,VACÍO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((2,4), [1], [UNO], (tablero), (tableroOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((2,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_sin_una_grilla(self):
        grillaUnoLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
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

        tablero = (grillaUnoLocal)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [UNO], (tablero), (tableroOponente)))


    def test_una_fila_menos(self):
        grillaUnoLocal = [[VACÍO, VACÍO],
                          [VACÍO, VACÍO],
                          [VACÍO, VACÍO]]
    
        grillaUnoOponente = [[VACÍO, VACÍO],
                             [VACÍO, VACÍO],
                             [VACÍO, VACÍO]]
    
        grillaDosLocal = [[VACÍO, VACÍO],
                          [VACÍO, VACÍO]]
    
        grillaDosOponente = [[VACÍO, VACÍO],
                             [VACÍO, VACÍO],
                             [VACÍO, VACÍO]]
    
        tablero = (grillaUnoLocal)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((3,2), [2], [UNO], (tablero), (tableroOponente))
    
        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((3,2), [2], [UNO], (tablero), (tableroOponente)))


    def test_fila_con_una_columna_mas(self):
        grillaUnoLocal      =   [[VACÍO, VACÍO], [VACÍO, VACÍO]]  # 2 columnas
        grillaUnoOponente   =   [[VACÍO, VACÍO], [VACÍO, VACÍO]]
        grillaDosLocal      =   [[VACÍO, VACÍO, VACÍO], [VACÍO, VACÍO]]  # ERROR: fila con 3 columnas
        grillaDosOponente   =   [[VACÍO, VACÍO], [VACÍO, VACÍO]]

        estado = ((2,2), [1], [UNO],(grillaUnoLocal, grillaUnoOponente),(grillaDosLocal, grillaDosOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((2,2), [1], [UNO],(grillaUnoLocal, grillaUnoOponente),(grillaDosLocal, grillaDosOponente)))


    def test_coinciden_posiciones(self):
        grillaUnoLocal = [[BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, BARCO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, BARCO]]

        grillaDosOponente = [[BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))

        self.assertTrue(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [UNO],(grillaUnoLocal, grillaUnoOponente),(grillaDosLocal, grillaDosOponente)))
    
    def test_no_coinciden_tablero1_tableroOponente0(self):
        grillaUnoLocal = [[BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, BARCO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, BARCO]]

        grillaDosOponente = [[BARCO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [UNO],(grillaUnoLocal, grillaUnoOponente),(grillaDosLocal, grillaDosOponente)))
    
    def test_no_coinciden_tableroOponente1_tablero0(self):
        grillaUnoLocal = [[BARCO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO]]

        grillaUnoOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, BARCO]]

        grillaDosLocal = [[VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, VACÍO],
                          [VACÍO, VACÍO, VACÍO, BARCO]]

        grillaDosOponente = [[VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, BARCO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO],
                             [VACÍO, VACÍO, VACÍO, VACÍO]]

        tablero = (grillaUnoLocal, grillaUnoOponente)
        tableroOponente = (grillaDosLocal, grillaDosOponente)

        estado = ((4,4), [1], [UNO], (tablero), (tableroOponente))

        self.assertFalse(esEstadoDeJuegoVálido(estado))
        self.assertEqual(estado, ((4,4), [1], [UNO],(grillaUnoLocal, grillaUnoOponente),(grillaDosLocal, grillaDosOponente)))


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
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_dos_tocado(self):
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
        self.assertEqual(resultado, TOCADO)
        self.assertEqual(estado, estado_esperado)

    def test_disparo_en_posicion_dos_vacia(self):
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
        self.assertEqual(resultado, NADA)
        self.assertEqual(estado, estado_esperado)


#Tests Ejercicio 5
class barcosEnGrilla_Test(unittest.TestCase):
    def test_varios_barcos_distintos_tamanios(self): # Varios barcos de distintos tamaños en una grilla con varios barcos de distintos tamaños
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



