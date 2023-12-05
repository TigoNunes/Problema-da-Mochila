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
        mochila_anterior = mochila[:]
        peso_objeto = objetos[i][1]
        for j in range(0, peso):
            if j >= peso_objeto:
                if mochila_anterior[j] < mochila_anterior[j - peso_objeto] + objetos[i][0]:
                    mochila[j] = mochila_anterior[j - peso_objeto] + objetos[i][0]
                    leva[j][i] = 1
    
    objetos_levados = []

    for i in range(peso - 1, -1, -1):
        cont = len(objetos) - 1
        for j in range(len(objetos) - 1, -1, -1):
            if leva[i][j] == 1:
                if objetos_levados.count(objetos[j]) <= 0:
                    objetos_levados.append(objetos[j])
                    i = i - objetos[j][1]
                    break
                else:
                    cont -= 1
            else:
                cont -= 1
                pass
        if not cont > 0:
            break
                    
    
    return objetos_levados, mochila[peso - 1]

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
        mochila, valor_total = Dinamico(objetos, peso + 1)
        enddinamico = time.time_ns()
        print(f"Itens na mochila: {mochila}\nValor na mochila: {valor_total}")
        _, peak = tracemalloc.get_traced_memory() #current and peak
        tracemalloc.stop()        
        times.append(enddinamico - startdinamico)
        memories.append((peak/(10**6)))

    times.sort()
    memories.sort()
    
    maior_tempo_dinamico = times[-1]
    tempo_medio_dinamico = (sum(times)/len(times))
    maior_memoria_dinamico = memories[-1]
    memoria_media_dinamico = (sum(memories)/len(memories))
    print(f"maior_tempo_dinamico: {maior_tempo_dinamico}\ntempo_medio_dinamico: {tempo_medio_dinamico}\nmaior_memoria_dinamico: {maior_memoria_dinamico}\nmemoria_media_dinamico: {memoria_media_dinamico}")
    print(f"maior_tempo_guloso: {maior_tempo_guloso}\ntempo_medio_guloso: {tempo_medio_guloso}\nmaior_memoria_guloso: {maior_memoria_guloso}\nmemoria_media_guloso: {memoria_media_guloso}")
    categorias = ['Guloso', 'Dinamico']
    valores = [tempo_medio_guloso, tempo_medio_dinamico]
    plt.bar(categorias, valores)
    plt.xlabel('Funções')
    plt.ylabel('Tempos (s)')
    plt.title('Tempos Médios')
    plt.show()

    categorias = ['Guloso', 'Dinamico']
    valores = [maior_tempo_guloso, maior_tempo_dinamico]
    plt.bar(categorias, valores)
    plt.xlabel('Funções')
    plt.ylabel('Tempos (s)')
    plt.title('Maiores tempos')
    plt.show()
    
    categorias = ['Guloso', 'Dinamico']
    valores = [memoria_media_guloso,memoria_media_dinamico]
    plt.bar(categorias, valores)
    plt.xlabel('Funções')
    plt.ylabel('Gasto de Memória (MB)')
    plt.title('Memória alocada Média')
    plt.show()

    categorias = ['Guloso', 'Dinamico']
    valores = [maior_memoria_guloso, maior_memoria_dinamico]
    plt.bar(categorias, valores)
    plt.xlabel('Funções')
    plt.ylabel('Gasto de Memória (MB)')
    plt.title('Memória mais altas alocada')
    plt.show()

if __name__ == '__main__':
    sys.exit(main())
    
