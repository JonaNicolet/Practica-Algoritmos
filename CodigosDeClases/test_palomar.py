from modulos import ListaDobleEnlazada
import unittest
import random


class Grafo:
    def get_nombre_vertices(self):
        return ['A', 'B', 'C']

def algoritmo_Prim(grafo:Grafo,inicio:Vertice):
    grafo_aem = None,
    costo_min = 1
    return grafo_aem, costo_min

class TestPalomasMensajeras(unittest.TestCase):
    """Test del sistema de mensajería"""

    def __init__(self):
        self.grafo_original = Grafo()
        # se cargan datos del grafo.
        self.grafo_original.agregarVertice('A')
        self.grafo_original.agregarVertice('B')
        self.grafo_original.agregarVertice('C')
        self.grafo_original.agregarArista('A','B',costo=1)
        self.grafo_original.agregarArista('B','C',costo=2)
        self.grafo_original.agregarArista('A','C',costo=3)
        self.grafo_original.agregarArista('B','A',costo=1)
        self.grafo_original.agregarArista('C','B',costo=2)
        self.grafo_original.agregarArista('C','A',costo=3)

        inicio = self.grafo_original.get_vertice('A') # Retorna un "Vertice"
        grafo_aem, costo_min = algoritmo_Prim(self.grafo_original, inicio)
        self.grafo_aem = grafo_aem
        self.distancia_total_aem = costo_min

    """"""
    def test_listado_aldeas(self):
        """Verifica que el listado de aldeas sea el correcto"""
        self.assertEqual(self.grafo_original.get_nombre_vertices(),
                         ['A', 'B', 'C'])
    

    def test_conexiones_aem(self):
        #test sobre de dónde llega el mensaje al nodo testeado
        #En función de cómo se pida la implementación, si el grafo puede devolver los vértices antecesores
        #para cada nodo, se puede chequear que esa lista tenga longitud unitaria para todos los nodos excepto
        #el de origen
        
        for vertice_elegido in self.__grafo.vertices:
            pass
        #chequear para algunos vértices elegidos aleatoriamente -> por eso importo random
        pass

    def test_distancia_total_aem(self):
        self.assertEqual(self.distancia_total_aem, 3)

if __name__ == '__main__':
    unittest.main()


