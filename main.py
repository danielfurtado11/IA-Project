from mapa import Mapa 
from grafo import Graph
from nodo import Node
import os
import time


def main():
    
    
    e = -1
    print("*************************************\n*             RACETRACK             *\n*************************************\n")
    print("MAPAS:\n    -> [1] - Mapa Praia     \U0001f3d6\uFE0F\n    -> [2] - Mapa Montanha  \u26F0\uFE0F\n    -> [3] - Mapa Deserto   \U0001f3dc\uFE0F")
    
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
        else:
            print("Opção inválida...")
    
    
    matrix = m.matrixMap()
    g = convertMapToGraph(matrix)
    saida = -1
    
    while saida != 0:
        print("\n**************************\n*          MENU          *\n**************************\n")
        print("-> [1] - Imprimir Mapa")
        print("-> [2] - Imprimir Grafo")
        print("-> [3] - Desenhar Grafo")
        print("-> [4] - Imprimir Nodos do Grafo")
        print("-> [5] - Imprimir Arestas do Grafo")
        print("-> [6] - DFS")
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
            print(g)
        
        elif saida == 3:
            g.desenha()

        elif saida == 4:
            print(g.m_graph.keys())
            
        elif saida == 5:
            print(g.imprime_aresta())
        
        elif saida == 6:
            start = m.getStart(matrix)
            #final = m.getFinal(matrix)
            print(g.procura_DFS(start,"33", path=[], visited=set()))
        
    
    
    

def convertMapToGraph(matrix):
    g  = Graph()
    i = j = 0
    largura = len(matrix[0])
    comprimento = len(matrix)

    
    
    for linha in matrix:
        for nodo in linha:
            if (i>0):
                custo = verificaPeca(nodo)
                n1 = f'{i}{j}'
                n2 = f'{i-1}{j}'
                g.add_edge(n1,n2,custo)
            if (i<largura-1):
                custo = verificaPeca(nodo)
                n1 = f'{i}{j}'
                n2 = f'{i+1}{j}'
                g.add_edge(n1,n2,custo)
            if (j>0):
                custo = verificaPeca(nodo)
                n1 = f'{i}{j}'
                n2 = f'{i}{j-1}'
                g.add_edge(n1,n2,custo)
            if (j<comprimento-1):
                custo = verificaPeca(nodo)
                n1 = f'{i}{j}'
                n2 = f'{i}{j+1}'
                g.add_edge(n1,n2,custo)

            i+=1
        j += 1
        i = 0
    return g


def verificaPeca(nodo):
    if nodo == 'X':
        return 25
    else:
        return 1
    
    
if __name__ == "__main__":
    main()
    
    
    
  