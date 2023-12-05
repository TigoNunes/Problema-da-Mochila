import random
with open("testes/teste5.txt", "a") as novo_teste:
    for i in range(10000):
        valor = random.randint(3, 10000)
        peso = random.randint(1, 1000)
        novo_teste.write(f"[{valor},{peso}], ")
    novo_teste.write("1000")