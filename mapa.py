from colorama import Fore, Back, Style


class Mapa:
    def __init__(self,name):
        self.m_name = str(name)
    
    def __str__(self):
        return "Mapa: " + self.m_name
    
    def __rep__(self):
        return "Mapa: " + self.m_name
    
    def getName(self):
        return self.m_name
    
    def setName(self, name):
        self.m_name = name
        
    def __eq__(self, other):
        return self.m_name == other.m_name
    
    def __hash__(self):
        return hash(self.m_name)
    
    
    
    def printMap(self):
        
        with open(self.m_name+".txt","r") as f:
                print(f.read())
    
    
    def matrixMap(self):
        
        with open(self.m_name+".txt", 'r') as f: 
            matrix = [[peca for peca in line[:-1].split(' ')] for line in f]
        
        #for linha in matrix:
        #    print(linha)
        #print('')
        return matrix
    
    def getStart(self,matrix):
        start = ([(row.index('P'),index) for index, row in enumerate(matrix) if 'P' in row])
        x, y = tuple(start[0])
        return (f'{y}.{x}')
        
    def getFinal(self,matrix):
        final = ([(row.index('F'),index) for index, row in enumerate(matrix) if 'F' in row])
        x , y = tuple(final[0])
        return (f'{y}.{x}')

    
    
    def showFinalmap(self,matrix,positionsList):
        
        for p in positionsList:
            parse = p.split('.')
            y = int(parse[0])
            x = int(parse[1])
            matrix[y][x] = "#"
        
        for linha in matrix:
            for peca in linha:
                if peca == "#":
                    print(Fore.RED + '# ' + Style.RESET_ALL, end='')
                else:
                    print(peca + ' ',end='')
            print()
            
        
    