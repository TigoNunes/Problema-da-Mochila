import sys
from menu import Menu
import tracemalloc #lib para metrificar memoria
import time #lib para métrificar o tempo
import matplotlib.pyplot as plt #lib para plotar os gráficos -> sudo apt install python3-pip -> pip install Matplotlib 
import copy

sys.setrecursionlimit(10**6)
def Guloso(objetos, capacidade):
    # Ordena a lista de objetos com base na razão valor/peso em ordem decrescente.
    objetos.sort(key=lambda x: x[0]/x[1], reverse=True)

    # Inicializa o valor total da mochila e uma lista para armazenar os itens selecionados.
    valor_total = 0.0
    mochila = []

    # Loop pelos objetos ordenados.
    for obj in objetos:
        # Desempacota os valores do objeto (valor, peso).
        valor, peso = obj
        # Se o peso do objeto for menor ou igual à capacidade restante da mochila.
        if peso <= capacidade:
            # Adiciona o objeto inteiro à mochila.
            capacidade -= peso
            valor_total += valor
            mochila.append((valor, peso))
        else:
            # Adiciona uma fração do objeto à mochila.
            fracao = capacidade / peso
            valor_total += valor * fracao
            mochila.append((valor * fracao, capacidade))
            # Sai do loop, pois a capacidade foi totalmente utilizada.
            break
    return valor_total, mochila


def Dinamico(objetos, peso):
    mochila = [0] * peso
    leva = [[0] * len(objetos) for _ in range(peso)]
    for i in range(0, len(objetos)):
        mochila_anterior = copy.deepcopy(mochila)
        peso_objeto = objetos[i][1]
        for j in range(0, peso):
            if j >= peso_objeto:
                if mochila_anterior[j] < mochila_anterior[j - peso_objeto] + objetos[i][0]:
                    mochila[j] = mochila_anterior[j - peso_objeto] + objetos[i][0]
                    leva[j][i] = 1
                    
    
    return mochila

def main():
    menu = Menu()
    teste = menu.teste
    peso = int(teste.pop(-1))
    objetos = [eval(ob) for ob in teste]
    
    
    #Rodando e pegando metricas do guloso
    times = []
    memories = []
    for i in range(0, 5):
        startGuloso = time.time()
        tracemalloc.start()
        valor_total, mochila = Guloso(objetos, peso + 1)
        endGuloso = time.time_ns()
        print("Valor Total da Mochila:", valor_total)
        _, peak = tracemalloc.get_traced_memory() #current and peak
        tracemalloc.stop()
        times.append(endGuloso - startGuloso)
        memories.append((peak/(10**6)))

    times.sort()
    memories.sort()
    
    maior_tempo_guloso = times[-1]
    tempo_medio_guloso = (sum(times)/len(times))
    maior_memoria_guloso = memories[-1]
    memoria_media_guloso = (sum(memories)/len(memories))
    
    times = []
    memories = []
    for i in range(0, 5):
        startdinamico = time.time()
        tracemalloc.start()
        print(Dinamico(objetos, peso + 1))
        _, peak = tracemalloc.get_traced_memory() #current and peak
        tracemalloc.stop()
        enddinamico = time.time()
        times.append(enddinamico - startdinamico)
        memories.append((peak/(10**6)))

    times.sort()
    memories.sort()
    
    maior_tempo_dinamico = times[-1]
    tempo_medio_dinamico = (sum(times)/len(times))
    maior_memoria_dinamico = memories[-1]
    memoria_media_dinamico = (sum(memories)/len(memories))
    
    categorias = ['Guloso', 'Dinamico']
    valores = [tempo_medio_guloso, tempo_medio_dinamico]
    plt.bar(categorias, valores)
    plt.xlabel('Funções')
    plt.ylabel('Tempos')
    plt.title('Tempos Médios')
    plt.show()

    categorias = ['Guloso', 'Dinamico']
    valores = [maior_tempo_guloso, maior_tempo_dinamico]
    plt.bar(categorias, valores)
    plt.xlabel('Funções')
    plt.ylabel('Tempos')
    plt.title('Maiores tempos')
    plt.show()
    
    categorias = ['Guloso', 'Dinamico']
    valores = [memoria_media_guloso,memoria_media_dinamico]
    plt.bar(categorias, valores)
    plt.xlabel('Funções')
    plt.ylabel('Gasto de Memória')
    plt.title('Memória alocada Média')
    plt.show()

    categorias = ['Guloso', 'Dinamico']
    valores = [maior_memoria_guloso, maior_memoria_dinamico]
    plt.bar(categorias, valores)
    plt.xlabel('Funções')
    plt.ylabel('Gasto de Memória')
    plt.title('Memória mais altas alocada')
    plt.show()

if __name__ == '__main__':
    sys.exit(main())
    
