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
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
from tkinter.ttk import *
from igraph import *
# segundo PLOT DE GRAFOS
import matplotlib.pyplot as plt
import networkx as nx # para funcionar o networkx é necessário pip install decorator==5.0.7
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#########################
# Criando a aplicação
#########################
class Application:

    #Funcção que cria o grafo conexo
    def criaGrafo(self):
        texto = ""
        a=[]
        v=n_vertice.get()
        a=n_aresta.get()

        #Iniciando o grafo
        G = nx.Graph()

        # Transformando a entrada as arestas em pares e adicionando as arestas ao grafo
        for i in range(len(a)):
            if (a[i] == "("):
                G.add_edge(a[i+1],  a[i+3], weight=0.1)


        # Monta as arestas com os pesos
        elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] >= 0.1]
    
        pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility
        
        # nós
        nx.draw_networkx_nodes(G, pos, node_size=700)

        # Arestas
        nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)

        # Títulos
        nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

        ax = plt.gca()
        ax.margins(0.08)
        plt.axis("off")
        plt.tight_layout()
        plt.show()
        

    #Função solicita as informações de vértices e arestas para criar um grafo
    def janelaGrafo(self):

       # label e input da quantidade de vértices 
       Label(root, text = "Informe a quantidade de vértices:").place(x = 40, y = 60)  
       self.qtd_vertices_input_area = Entry(root, textvariable = n_vertice, width = 10).place(x = 230,y = 60) 
       
       # label e input das arestas 
       Label(root, text = "Infome as arestas:").place(x = 40, y = 100)
       Label(root, text = "Exemplo de preenchimento: (0,1),(1,2),(2,3),(3,4),(3,5),(5,3)").place(x = 220, y = 120)
       
       self.arestas_input_area = Entry(root, textvariable = n_aresta, width = 30).place(x = 230, y = 100)

       # Botão que Chama a função de criar o grafo
       self.submit_button = Button(root, text = "Submit", command =self.criaGrafo).place(x = 40, y = 130)


    def donothing(self):
        labelExample = tk.Label(root,text=" entei aqui ")
        labelExample.pack()
       
    #Função inicial que cria o frame com menu de opções
    def __init__(self, root):

        #Criando o título do frame
        root.title("Sobrevivência de Rede")
        #Setando o tamanho do frame
        root.geometry('600x300')

        #Criando o Menu de opções
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Criar grafo conexo", command=self.janelaGrafo)
        
        filemenu.add_command(label="Gerar falhas no grafo conexo", command=self.donothing)
        filemenu.add_command(label="Algoritmo Exato", command=self.donothing)
        filemenu.add_command(label="Algoritmo Aproximado", command=self.donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="Início", menu=filemenu)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.donothing)
        helpmenu.add_command(label="About...", command=self.donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
      
        root.config(menu=menubar)
        root.mainloop()


#########################
# Programa Principal
#########################
if __name__ == "__main__":
    #Criando a janela principal
    root = tk.Tk()

    #Inicializando variáveis
    n_vertice=tk.StringVar()
    n_aresta=tk.StringVar()

    #Criando o frame da janela principal
    Application(root)
    