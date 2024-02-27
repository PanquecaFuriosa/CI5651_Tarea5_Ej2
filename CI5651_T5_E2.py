from queue import Queue
 
INF = 999999999
NIL = 0
 
# Clase para implementar el grafo bipartito con su algoritmo Hopcroft-Karp
class GrafoBipartito:

    def __init__(self, m, n):
        
        self.m = m
        self.n = n
        self.adj = [[] for _ in range(m + 1)]
        self.cU, self.cV, self.dist = None, None

 
    def agregarArista(self, u, v):
        self.adj[u].append(v)  
 
    def bfsHopcroftKarp(self):
        Q = Queue()
        for u in range(1, self.m + 1):
            if (self.cU[u] == NIL):
                self.dist[u] = 0
                Q.put(u)
            else:
                self.dist[u] = INF

        self.dist[NIL] = INF

        while (not Q.empty()):
            u = Q.get()
            if (self.dist[u] < self.dist[NIL]):
                for v in self.adj[u]:
                    if (self.dist[self.cV[v]] == INF):
                        self.dist[self.cV[v]] = self.dist[u] + 1
                        Q.put(self.cV[v])

        return self.dist[NIL] != INF
 
    def dfsHopcroftKarp(self, u):
        if (u != NIL):
            for v in self.adj[u]:
                if self.dist[self.cV[v]] == self.dist[u] + 1:
                    if self.dfsHopcroftKarp(self.cV[v]):
                        self.cV[v] = u
                        self.cU[u] = v
                        return True

            self.dist[u] = INF
            return False

        return True
 
    def hopcroftKarp(self):
        self.cU = [0 for _ in range(self.m + 1)]
        self.cV = [0 for _ in range(self.n + 1)]
        self.dist = [0 for _ in range(self.m + 1)]

        r = 0

        while (self.bfsHopcroftKarp()):
            for u in range(1, self.m + 1):
                if (self.cU[u] == NIL and self.dfsHopcroftKarp(u)):
                    r += 1

        return r

# Funciones para saber si un numer es primo
def criba_eratostenes(n):
    primos = [True for i in range(n + 1)]
    p = 2
    while ((p * p) <= n):
        if (primos[p] == True):
            for i in range(p * p, n + 1, p):
                primos[i] = False
        p += 1

    # No se consideran primos
    primos[0]= False
    primos[1]= False

    return [p for p in range(2, n) if primos[p]]
    
def es_primo(n):
    return n in (criba_eratostenes(n + 1))

# Función para crear un grafo bipartito con dos conjuntos, pares e impares
def crear_grafo_bipartito(P, I):
    G = GrafoBipartito(len(P), len(I))

    for i in range(len(P)):
        for j in range(len(I)):
            if es_primo(P[i] + I[j]):
                G.agregarArista(i, j)

    return G

def main(C):
    P = [x for x in C if x % 2 == 0]
    I = [x for x in C if x % 2 != 0]
    G = crear_grafo_bipartito(len(P), len(I))
    r = G.hopcroftKarp()

    return r
