from leitor import Leitor

class Menu:
    def __init__(_self):
        _self.teste:str
        _self.opcoes()
    
    def opcoes(_self):
        escolha = input("Qual teste executar?\nTeste 0: teste padrão\nTeste 1: 10 números\nTeste 2: 100 números\nTeste 3: 1000 números\nTeste 4: 5000 números\nTeste 5: 10000 números\n>> ")
        leitor = Leitor(f"teste_{escolha}")
        _self.teste = leitor.teste