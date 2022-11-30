from mapa import Mapa 
import os
import time
from newSearch import newSearch


def main():
    
    
    e = -1
    print("*************************************\n*             RACETRACK             *\n*************************************\n")
    print("MAPAS:\n    -> [1] - Mapa Praia     \U0001f3d6\uFE0F\n    -> [2] - Mapa Montanha  \u26F0\uFE0F\n    -> [3] - Mapa Deserto   \U0001f3dc\uFE0F\n    -> [4] - Mapa Pista     \U0001f3c1")
    while 1:
        e = int(input("Escolha o seu mapa: "))

        if (e == 1):
            m = Mapa("Praia")
            os.system('clear')
            break
        elif (e == 2):
            m = Mapa("Montanha")
            os.system('clear')
            break
        elif (e == 3):
            m = Mapa("Deserto")
            os.system('clear')
            break
        elif (e == 4):
            m = Mapa("Pista")
            os.system('clear')
            break
        else:
            print("Opção inválida...")
    
    
    map = m.matrixMap()
    #map2 = m.matrixMap()
    start = m.getStart(map)
    final = m.getFinal(map)
    st =    start.split('.')
    tuple = (int(st[0]),int(st[1]))
    solve = newSearch(map,tuple)
    solve.convertMapToGraph()
    graph = solve.g
    map1 = m.matrixMap()
    
    
    saida = -1
    
    while saida != 0:
        print("\n**************************\n*          MENU          *\n**************************\n")
        print("-> [1] - Imprimir Mapa")
        print("-> [2] - Imprimir Grafo")
        print("-> [3] - Imprimir Nodos do Grafo")
        print("-> [4] - Imprimir Arestas do Grafo")
        print("-> [5] - DFS")
        print("-> [6] - BFS")
        print("-> [0] - Sair\n")
        saida = int(input("Escolha uma opção: "))
        print('\n')
        if saida == 0:
            print("Terminando Programa...")
            time.sleep(2)
            os.system('clear')

        elif saida == 1:
            m.printMap()
    
        elif saida == 2:
            print(graph)

        elif saida == 3:
            print(graph.m_graph.keys())
            
        elif saida == 4:
            print(graph.imprime_aresta())
        
        elif saida == 5:
            result = graph.procura_DFS(start,final, path=[], visited=set())
            print(result)
            print('\n')
            m.showFinalmap(map,result[0])
            
        elif saida == 6:
            print(start)
            print(final)
            result = graph.procura_BFS(start,final)
            print(result)
            print('\n')
            m.showFinalmap(map1,result[0])
        

    
if __name__ == "__main__":
    main()
    
    
    
  