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
from tkinter.ttk import *
from igraph import *


#########################
# Criando a aplicação
#########################
class Application:

    # declaring string variable
    # for storing name and password 

    def grafo(self):
       texto = ""
       v=n_vertice.get()
       a=n_aresta.get()
       
       eG=Graph(directed=False)
       eG.add_vertices(6)
       eG.add_edges([(0,1),(1,2),(2,3),(3,4),(3,5),(5,3)])
       eG.es['weight']=[12,1,2,3,4,1]

       layout = eG.layout("kk")

       visual_style = {}
       visual_style["vertex_size"] = 20
       visual_style["vertex_label"] = ["a","b","c","d","e","f"]
       visual_style["edge_width"] = eG.es['weight']
       visual_style["bbox"] = (300, 300)
       plot(eG, **visual_style)
       texto = ("Grafo gerado com ", v ," vértices e as seguintes arestas: ", a)
       labelExample = tk.Label(root, text=texto).place(x = 40, y = 160)

    def doAlgo(self):
       # label e input da quantidade de vértices 
       qtd_vertices = Label(root, text = "Informe a quantidade de vértices:").place(x = 40, y = 60)  
       qtd_vertices_input_area = Entry(root, textvariable = n_vertice, width = 10).place(x = 230,y = 60) 

       
       # label e input das arestas 
       arestas = Label(root, text = "Infome as arestas:").place(x = 40, y = 100)
       Label(root, text = "Exemplo de preenchimento: (0,1),(1,2),(2,3),(3,4),(3,5),(5,3)").place(x = 220, y = 120)
       
       arestas_input_area = Entry(root, textvariable = n_aresta, width = 30).place(x = 230, y = 100)

       #Chama a função de criar o grafo
       submit_button = Button(root, text = "Submit", command =self.grafo).place(x = 40, y = 130)


       

    def donothing(self):
        labelExample = tk.Label(root,text=" entei aqui ")
        labelExample.pack()
       
    def __init__(self, master=None):

        #Criando o título do frame
        root.title("Sobrevivência de Rede")
        #Setando o tamanho do frame
        root.geometry('600x300')

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
    #Criando a janela principal
    root = tk.Tk()

    n_vertice=tk.StringVar()
    n_aresta=tk.StringVar()

    #Criando o frame da janela principal
    Application(root)
    