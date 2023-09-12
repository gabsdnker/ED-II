#Nome: Gabrielli Danker     Matéria: Estrutura de Dados II 

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

    def bfs(self, inicio):
        visitados = {}
        fila = []
        for v in self.vertices:
            visitados[v] = False
        fila.append(inicio)
        visitados[inicio] = True

        while fila:
            vertice = fila.pop(0)
            print(vertice, end=" -> ")
            for vizinho in self.adj(vertice):
                if not visitados[vizinho]:
                    fila.append(vizinho)
                    visitados[vizinho] = True
        print("Fim")

    def dfs(self, inicio):
        visitados = {}
        for v in self.vertices:
            visitados[v] = False
        self._dfs_recursivo(inicio, visitados)

    def _dfs_recursivo(self, vertice, visitados):
        print(vertice, end=" -> ")
        visitados[vertice] = True
        for vizinho in self.adj(vertice):
            if not visitados[vizinho]:
                self._dfs_recursivo(vizinho, visitados)
                
    def imprime_caminho(self, inicio, fim):
        visitados = {}
        caminho = []
        for v in self.vertices:
            visitados[v] = False
        self._encontra_caminho(inicio, fim, visitados, caminho)
        print("Caminho de", inicio, "a", fim, ":", caminho)

    def _encontra_caminho(self, atual, fim, visitados, caminho):
        visitados[atual] = True
        caminho.append(atual)
        if atual == fim:
            return
        for vizinho in self.adj(atual):
            if not visitados[vizinho]:
                self._encontra_caminho(vizinho, fim, visitados, caminho)

def main():
    grafo = GrafoNaoDirigido()
    grafo.insereV('A')
    grafo.insereV('B')
    grafo.insereV('C')
    grafo.insereV('D')
    grafo.insereV('E')

    grafo.insereA('A', 'B')
    grafo.insereA('B', 'C')
    grafo.insereA('C', 'D')
    grafo.insereA('C', 'E')

    print("Ordem do grafo:", len(grafo.vertices))  # Saída: 5
    print("Tamanho do grafo:", len(grafo.arestas()))  # Saída: 6
    print("Vértices adjacentes a 'D':", grafo.adj('D'))  # Saída: ['C']
    print("Grau de 'D':", grafo.grau('D'))  # Saída: 1
    print("Arestas do grafo:", grafo.arestas())  # Saída: [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B'), ('C', 'D'), ('C', 'E'), ('D', 'C'), ('E', 'C')]

    print(grafo)  # Saída formatada do grafo

    print("Busca em Largura:")
    grafo.bfs('A')  # Exemplo de BFS a partir do vértice 'A'

    print("\nBusca em Profundidade:")
    grafo.dfs('A')  # Exemplo de DFS a partir do vértice 'A'

    print("\nCaminho entre 'A' e 'D':")
    grafo.imprime_caminho('A', 'D')  # Exemplo de impressão de caminho entre 'A' e 'D'

if __name__ == "__main__":
    main()