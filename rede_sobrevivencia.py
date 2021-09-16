##################################
#PROJETO FINAL
# Data: 11/08/2021
#Autores: Paulo, Priscilla, Wagner
##################################

"""
NETWORK SURVIVABILITY (qual a probabilidade de sobrevivência da rede, força bruta, sobrevive a qualquer ataque, falhas individuais, isoladas, gargalos, ponto frágil)
INSTANCE: Graph G = (V, E), a rational "failure probability" p(x), 0 ≤ p(x) ≤ 1, for each x ϵ V υ E, a positive rational number q ≤ 1.
QUESTION: Assuming all edge and vertex failures are independent of one another, is the probability q or greater that for all {u, v} ϵ E at least one of u,v ou {u, v} will fail?

A analise sera realizada em tres etapas: 
a) configuracao do ambiente de execucao, com a carga do grafo que representa a rede a ser avaliada; 
b) geracao e distribuicao aleatoria dos valores correspondentes as probabilidades de falha de cada um dos elementos do grafo, bem como da probabilidade de sobrevivencia geral do grafo, e; 
c) deteccao dos elementos com falhas eventuais e submissao do grafo derivado as heurısticas de avaliacao de sobrevivencia da rede.

"""
#########################
# Imports necessários
#########################
import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk


from tkinter import *
from matplotlib import patches
from tkinter.ttk import *
from igraph import *
# segundo PLOT DE GRAFOS
import matplotlib.pyplot as plt
import networkx as nx # para funcionar o networkx é necessário pip install decorator==5.0.7
import matplotlib
matplotlib.use('TkAgg')
import random 
from itertools import  combinations, groupby
import matplotlib.patches as mpatches
import dwave_networkx as dnx
import dimod
import time
import pandas as pd




#########################
# Criando a aplicação
#########################
class Application:

    G = nx.Graph()
    G2 = nx.Graph()
    resultadoAnalise = list()
    
    campos = ['execucoes','verticesG','arestasG', 'verticesG2','arestasG2',
              'nodeConnectivityG', 'timeNodeConnectivityG', 'diametroG', 'timeDiametroG',
              'pontesG', 'timePontesG', 'conexoPorPonteG2', 'timeConexoPorPonteG2',
              'dfsFBG2', 'timeDfsFBG2',  'dfsOtimizadoBG2', 'timeDfsOtimizadoG2',
              'conexoPorTSP', 'timeConexoPorTSP']    

    '''
    Função geraProbabilidadeSobrevivencia: Gera probabilidades acima de 70% de sobrevivência da rede
    Entradas:
        Faixa de probabilidade entre 0.7 a 1 por padrão
    Saída:
        apresenta os números gerados
    '''
    def geraProbabilidadeSobrevivencia(self, start=0.7):
        return random.uniform(start, 1)
         
    '''
    Função geraProbabilidadeFalha: Gera as probabilidades de falhas de cada aresta
    Entradas:
        Faixa de probabilidade entre 0 e 1
    Saída:
        Probabilidade
    '''
    def geraProbabilidadeFalha(self, start, end):
       return random.uniform(start, end)
   
    
    '''
        Cria grafo conexo não completo
        1 geração do grafo G com respectivas probabilidades de falhas 
        2 
    '''
    def criaGrafoConexo(self,n, p=0.02):
        edges = combinations(range(n), 2)
        G = nx.Graph()
        G.add_nodes_from(range(n))
        if p <= 0:
            return G
        if p >= 1:
            return nx.complete_graph(n, create_using=G)
        for _, node_edges in groupby(edges, key=lambda x: x[0]):
            node_edges = list(node_edges)
            
            random_edge = random.choice(node_edges)
            G.add_edge(random_edge[0],random_edge[1], probability = self.geraProbabilidadeFalha(0, 1))
            for e in node_edges:
                if random.random() < p:
                    G.add_edge(e[0],e[1], probability = self.geraProbabilidadeFalha(0, 1))

        return G

       
        
    '''
    Função drawGraph: apresenta o grafo visualmente
    Entradas:
        grafo
    Saída:
        apresenta o grafo construído
    '''
    def drawGraph(self):
        graphs = []
        graphs.append(self.G)
        graphs.append(self.G2)
        
        # duas linhas e 1 coluna
        fig, axes = plt.subplots(nrows=2, ncols=1)
        ax = axes.flatten()
        
        
        # # Add the legend manually to the current Axes.
 

        
        for i in range(len(graphs)):
            ax[i].set_axis_off()
            plt.tight_layout()
            
            
            original = patches.Patch(color='blue', label='G1')
            podado = patches.Patch(color='green', label= 'G2')
            
            superior = plt.legend(handles=[original], loc='upper right')
            inferior = plt.legend(handles=[podado], loc='lower right')
            
            plt.gca().add_artist(superior)
            plt.gca().add_artist(inferior)
        
            nx.draw_networkx(graphs[i], ax=ax[i])
            
            plt.show()
            


    

    '''
    Função removeElementos: Remove arestas do grafo G2
    Entradas:
        arestas

    '''
    def removeElementos(self): 
        #gera probabilidade de sobrevivencia da rede
        q = self.geraProbabilidadeSobrevivencia()
        #Listas de elementos a serem removidos (os que tiverem probabilidade de 
        #falha maior que a probabilidade de sobrevivencia da rede)
        removerElementos = [(u, v) for (u, v, d) in self.G2.edges(data=True) if d["probability"] > q]
        #remove elementos
        self.G2.remove_edges_from(removerElementos)
        return 


    '''
    Função isGrafoConexo: Verifica se um grafo é conexo 
    Entradas:
        grafo
    Saída:
        retorna se o grafo é conexo ou não
    '''
    def isGrafoConexoConnectedComponents(self):
        return (len(list(nx.connected_components(self.G2))) == 1)


    def printVertexCover(self):
        lstVertex = []
        isVertexCover = False
        cover = (list(self.G2.adj))
        isVertexCover = dnx.is_vertex_cover(self.G2,cover)
        sampler = dimod.ExactSolver()
        lstVertex = dnx.min_vertex_cover(self.G, sampler, lagrange=2.0)
        #print('É vertex cover: ', isVertexCover)
        #print('Lista de vertex cover: ', *lstVertex)


    '''
    Função listAutores: Apresenta os desenvolvedores do programa
    Entradas:
    Saída:
        Apresentação do texto 
    '''
    def listAutores(self):
        autores =('Universidade de Brasília – UnB\n\n')
        autores+=('Programa de Pós-Graduação em Computação Aplicada - PPCA\n\n')
        autores+=('Programa desenvolvido como requisito da Disciplina AED - Algoritmos e Estruturas de Dados\n\n Professor: Edison Ishikawa\n\n')
        autores+=('Alunos: Marcio\nPaulo Rezende\nPriscilla Alves\nWagner Costa\n\n')
        autores+=('Versão: 1.0\nMês e Ano: 09/2021')
        self.resTexto(autores)
        
    '''
    Função resTexto: Modifica o texto da Label texto
    Entradas:
        Texto
    Saída:
        Apresentação do texto 
    '''
    def resTexto(self, res):
        frame_texto.config(text=res)           
        
        
        
    def executaDemonstracao(self):

        self.resultadoAnalise = list()
        self.resultadoAnalise.append(self.campos)
        self.executaProcedimentos(1, 25, .1)
        self.drawGraph()

        #gera arquivo com estatisticas
        filename = 'est' + time.strftime("%Y%m%d%H%M%S") + '.csv'
        pd.DataFrame(self.resultadoAnalise).to_csv(filename, index=False, header=False)
        print('FIM')
        return


    def executaAnalise(self):

        self.resultadoAnalise = list()
        self.resultadoAnalise.append(self.campos)
        
        a = [250,500,1000,1500,2000,3000]

        for arestas in a:
        #for arestas in range(10, 60, 10):
            print('Executa analise', str(arestas), str(arestas/100000))
            start = time.perf_counter()
            self.executaProcedimentos(10, arestas, arestas/100000)
            print('\n', str(time.perf_counter()-start))
            

        #gera arquivo com estatisticas
        filename = 'est' + time.strftime("%Y%m%d%H%M%S") + '.csv'
        pd.DataFrame(self.resultadoAnalise).to_csv(filename, index=False, header=False)
        print('FIM')
        return
    
    
    
    def executaProcedimentos(self, qtdeExecucoes, qtdVertices, probabilidadeAdjacencia):
        
        
        
        #cria grafo original conexo
        self.G = self.criaGrafoConexo(qtdVertices, probabilidadeAdjacencia)
        
        #executa os procedimentos, registrando os resultados em dicionario
        for i in range(0, qtdeExecucoes):
            print('.', end='')
            #limpa G2
            self.G2.clear()
            #criar uma copia de G em G2
            self.G2 = self.G.copy()
            #remove elementos em G2
            self.removeElementos()
            #roda algoritimos e heuristicas
            self.executaAlgoritmos(qtdeExecucoes, qtdVertices)
        #end if
        

        return
    
    
    def executaAlgoritmos(self, qtdeExecucoes, qtdVertices):
        log = []
        log.append(qtdeExecucoes)

        #vértices G
        log.append(self.G.number_of_nodes())
        #arestas G
        log.append(self.G.size())

        #vértices G2
        log.append(self.G2.number_of_nodes())        
        #arestas G2
        log.append(self.G2.size())
        
        #node connectivity G
        start = time.perf_counter()
        log.append(nx.approximation.node_connectivity(self.G))
        #tempo node connectivity G
        log.append(time.perf_counter() - start)
        
        #diâmetro G
        start = time.perf_counter()
        log.append(nx.algorithms.approximation.distance_measures.diameter(self.G))
        #tempo diâmetro G
        log.append(time.perf_counter() - start)
        
        #pontes G
        start = time.perf_counter()
        bridges = list(nx.bridges(self.G))
        log.append(len(bridges))
        #tempo pontes G
        log.append(time.perf_counter() - start)

        #verifica conectividade em G2, confirmando se todas as pontes em G
        #permanecem em G2. Caso alguma tenha sido removida, G2 se torna desconexo
        start = time.perf_counter()
        g2Conexo = True
        for edge in bridges: 
            g2Conexo = self.G2.has_edge(edge[0], edge[1])
            if not g2Conexo:
                break
            #end if
        #end for        
        log.append(int(g2Conexo))
        #tempo verificação de conectividade via pontes
        log.append(time.perf_counter() - start)
        

        #DFS força-bruta G2        
        start = time.perf_counter()
        log.append(len(list(nx.dfs_edges(self.G2, source=0))))
        #tempo DFS força-bruta G2
        log.append(time.perf_counter() - start)

        #DFS otimizado G2
        start = time.perf_counter()
        log.append(len(list(nx.edge_dfs(self.G2))))
        #tempo DFS otimizado G2
        log.append(time.perf_counter() - start)
        
        #TSP força-bruta G2
        start = time.perf_counter()
        try:
            tsp = len(nx.approximation.traveling_salesman_problem(self.G2, cycle=False))
            log.append(int(True))
        except KeyError:
            #erro ocorre quando se tenta fazer TSP em grafo não-conexo
            log.append(int(False))
            
        #tempo TSP força-bruta G2
        log.append(time.perf_counter() - start)
        
        self.resultadoAnalise.append(log)

        return
 
            


    '''
    Função __init__
    Entradas:
        Frame da janela principal do sistema
    Saída:
        Tela principal do sistema com menus de opçoes
    '''
    def __init__(self, root):

        #Criando o título do frame
        root.title("Sobrevivência de Rede")
        #Setando o tamanho do frame
        root.geometry('600x300')

        #Criando o Menu de opções
        menubar = tk.Menu(root)
        filemenu = tk.Menu(menubar, tearoff=0)

        # add the File menu to the menubar
        filemenu.add_command(label="Demonstração" , command=self.executaDemonstracao)
        filemenu.add_command(label="Análise" , command=self.executaAnalise)
        filemenu.add_separator()
        filemenu.add_command(label="Sair", command=root.quit)
        menubar.add_cascade(label="Início", menu=filemenu)
        
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Autores", command=self.listAutores)
        menubar.add_cascade(label="Sobre", menu=helpmenu)
    
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

    #Criando o frame de texto    
    frame_texto = Label(root, text= '', justify='center', font=('Times New Roman', 12))
    frame_texto.pack()   

    #Criando o frame da janela principal
    Application(root)
    