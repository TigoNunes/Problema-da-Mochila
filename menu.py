from leitor import Leitor

class Menu:
    def __init__(_self):
        _self.teste:str
        _self.opcoes()
    
    def opcoes(_self):
        escolha = input("Qual teste executar?\nTeste 0: teste padrão\nTeste 1: 10 itens\nTeste 2: 100 itens\nTeste 3: 1000 itens\nTeste 4: 5000 itens\nTeste 5: 10000 itens\n>> ")
        leitor = Leitor(f"teste{escolha}")
        _self.teste = leitor.teste