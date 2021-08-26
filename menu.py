#!/usr/bin/python
# coding: utf-8

# Este programa é um exemplo de implementação direta (sem usar estruturas
# elaboradas) do algoritmo de Dijkstra

# Baseado no algoritmo descrito no livro "Algoritmos: Teoria e Prática"
#   A fila de prioridade é implementado fazendo um busca linear em um
#   no vetor de estimativas de menores distâncias, semelhante a
#   implementação de fila de prioridade do algoritmo de Prim do
#   exercício 23.2-2
#########################
# Imports necessários
#########################
import tkinter as tk


#########################
# Criando a aplicação
#########################
class Application:
    def doAlgo(self):
       retorno = teste()
       #print(retorno)
       labelExample = tk.Label(text=retorno)
       labelExample.pack()

    def donothing(self):
        labelExample = tk.Label(text=" ")
        labelExample.pack()
       
    def __init__(self, master=None):

        #Criando o título do frame
        root.title("Sobrevivência de Rede")
        #Setando o tamanho do frame
        root.geometry('400x300')

        #Criando o Menu de opções
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Criar grafo conexo", command=self.doAlgo)
        
        filemenu.add_command(label="Gerar falhas no grafo conexo", command=self.donothing)
        filemenu.add_command(label="Algoritmo Exato", command=self.donothing)
        filemenu.add_command(label="Algoritmo Aproximado", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=root.quit)
        menubar.add_cascade(label="Início", menu=filemenu)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
      
        root.config(menu=menubar)
        root.mainloop()

#########################
# Funções da Dijkstra
#########################
def initialize_single_source(g, s):
    n = len(g)
    d = [None] * n
    pai = [None] * n
    for v in range(n): # for each v in g.V
        d[v] = float("+infinity")
        pai[v] = None
    d[s] = 0
    return d, pai

def extract_min(Q, S):
    n = len(Q)
    min = None
    for v in range(n): # for each v in g.V
        if not S[v]:
           if min == None:
               min = v
           elif Q[v] < Q[min]:
               min = v
    return min

def dijkstra(g, s):
    d, pai = initialize_single_source(g, s)
    n = len(g)
    S = [False] * n # atributo do vértice que indica se
                    # ele faz parte da árvore de caminhos mínimos
    Q = d           # a fila de prioridade é o próprio vetor de
                    # estimativas de menor distância
    for i in range(n):
        u = extract_min(Q, S)
        S[u] = True # vértice adicionado a árvore de caminhos mínimos
        for w, v in g[u]: # w é o peso da aresta (u, v)
            if d[v] > d[u] + w:
                d[v] = d[u] + w
                pai[v] = u
                # decrease-key não é necessário
                # a lista Q é uma reverência para a lista d
                # como a lista d foi altera, Q também foi
    return d, pai

def teste():
    # cada elemento da lista de adjacências do vértice u é uma tupla (w, v)
    # onde w é o peso da aresta (u, v)
    # grafo da figura 24.6
    g = [
        [(10, 1), (5, 3)],
        [(1, 2), (2, 3)],
        [(4, 4)],
        [(3, 1), (9, 2), (2, 4)],
        [(7, 0), (6, 2)]
    ]

    d, pai = dijkstra(g, 0)

    assert d ==  [0, 8, 9, 5, 7]     
    #print ("d =", d)

    assert pai == [None, 3, 1, 0, 3]
    return pai


#########################
# Programa Principal
#########################
if __name__ == "__main__":
    #teste()
    root = tk.Tk()
    Application(root)
    