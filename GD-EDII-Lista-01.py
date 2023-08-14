#Gabrielli Danker       ED II 

class GrafoNaoDirigido:
    def __init__(self):
        self.vertices = {}  # Um dicionário onde as chaves são vértices e os valores são listas de vértices adjacentes.
    
    def insereV(self, v):
        if v not in self.vertices:
            self.vertices[v] = []
    
    def removeV(self, v):
        if v in self.vertices:
            for adjacente in self.vertices[v]:
                self.vertices[adjacente].remove(v)
            del self.vertices[v]
    
    def insereA(self, u, v):
        if u in self.vertices and v in self.vertices:
            if v not in self.vertices[u]:
                self.vertices[u].append(v)
            if u not in self.vertices[v]:
                self.vertices[v].append(u)
    
    def removeA(self, u, v):
        if u in self.vertices and v in self.vertices:
            if v in self.vertices[u]:
                self.vertices[u].remove(v)
            if u in self.vertices[v]:
                self.vertices[v].remove(u)
    
    def adj(self, v):
        return self.vertices[v]
    
    def getA(self, u, v):
        if u in self.vertices and v in self.vertices:
            if v in self.vertices[u]:
                return (u, v)
        return None
    
    def grau(self, v):
        return len(self.vertices[v])
    
    def verticesA(self, e):
        u, v = e
        return (u, v)
    
    def arestas(self):
        arestas = []
        for v, adjacentes in self.vertices.items():
            for adjacente in adjacentes:
                arestas.append((v, adjacente))
        return arestas
    
    def __str__(self):
        result = "Vértices:\n"
        for vertex in self.vertices:
            result += f"{vertex}: {self.vertices[vertex]}\n"
        result += "Arestas:\n"
        for edge in self.arestas():
            result += f"{edge}\n"
        return result

def main():
    grafo = GrafoNaoDirigido()
    grafo.insereV('A')
    grafo.insereV('B')
    grafo.insereV('C')
    grafo.insereA('A', 'B')
    grafo.insereA('B', 'C')

    print("Ordem do grafo:", len(grafo.vertices))  # Saída: 3
    print("Tamanho do grafo:", len(grafo.arestas()))  # Saída: 2
    print("Vértices adjacentes a 'B':", grafo.adj('B'))  # Saída: ['A', 'C']
    print("Grau de 'B':", grafo.grau('B'))  # Saída: 2
    print("Arestas do grafo:", grafo.arestas())  # Saída: [('A', 'B'), ('B', 'C')]

    print(grafo)  # Saída formatada do grafo

if __name__ == "__main__":
    main()
