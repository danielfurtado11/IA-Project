from queue import Queue
from grafo import Graph

class newSearch:
    
    
    def __init__(self, matrix,start):
        self.matrix = matrix
        self.g = Graph(directed=True)    
        self.start = start
        

    
    def convertMapToGraph(self):
        
        height, width = len(self.matrix), len(self.matrix[0])
        
        visited = []
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]     # estados possíveis
        
        
        queue = Queue()
        
        queue.put(self.start)
        
        
        while not queue.empty():
            coord = queue.get()
            visited.append(coord)
            if self.matrix[coord[0]][coord[1]] == "F":
                return visited
            
            for dir in directions:
                
                heightC, widthC = coord[0]+dir[0], coord[1]+dir[1]
                if (heightC < 0 or heightC >= height or widthC < 0 or widthC >= width or self.matrix[heightC][widthC] == "X" or (heightC,widthC) in visited): continue      # condição para criar o mapa
                coords = str(coord[0])+       '.'                +  str(coord[1])
                coords1 = str(heightC)+       '.'                +  str(widthC)
                self.g.add_edge(coords,coords1,1)
                queue.put((heightC,widthC))
    
