""" AND = para ser True tudo tem que ser True; """
""" OR = para ser True apenas um precisa ser True; """


print("-----OPERADORES LÓGICOS-----")
print("True and True = ", True and True)
print("True and False = ", True and False)
print("False and False = ", False and False)
print("True or True = ", True or True)
print("True or False = ", True or False)
print("False or False = ", False or False)


saldo = 2000;
saque = 300;
limite = 200;
conta_banco = True;

print("\n PARTE DAS EXPRESSÕES:")

""" JEITO DIFÍCIL DE ANALISAR E ENCHERGAR: """
expressao1 = saldo >= saque and saque <= limite or conta_banco and saldo >= saque;
print(expressao1)

""" JEITO FÁCIL DE ANALISAR E ENCHERGAR: """
expressao2 = (saldo >= saque and saque <= limite) or (conta_banco and saldo >= saque);
print(expressao2)

""" JEITO PROFISSIONAL DE SE USAR, QUE FACILITA MAIS AINDA A ANALISE: """
conta_normal_com_saldo_suficiente = saldo >= saque and saque <= limite;
conta_banco_com_saldo_suficiente = conta_banco and saldo >= saque;

expressao3 = conta_normal_com_saldo_suficiente or conta_banco_com_saldo_suficiente;
print(expressao3)