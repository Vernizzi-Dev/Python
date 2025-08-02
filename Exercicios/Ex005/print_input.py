name = input("Digite o seu nome: ")
idade = int(input("Insira a sua idade: "))

""" saída normal 👇 """
print(name, idade)
""" saída apenas com o end 👇 """
print(name, idade, end="...\n")
""" saída apenas com o sep (separador) 👇"""
print(name, idade, sep=" --- ")
""" saída com o end e o sep 👇 """
print(name, idade, sep=" --- ", end="...\n")