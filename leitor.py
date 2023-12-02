class Leitor:
    def __init__(self, teste:str):
        with open (f"testes/{teste}.txt") as arquivo:
            dados = arquivo.read()
            t = dados.split(", ")
            self.teste = []
            try:
                for letra in t:
                    self.teste.append(int(letra))
            except:
                pass