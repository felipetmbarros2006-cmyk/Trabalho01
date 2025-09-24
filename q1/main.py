# Questão 1 - Manipulação de listas e strings

from funcoes import contar_palavra


frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra para buscar: ")

quantidade = contar_palavra(frase, palavra)

# Quantidade de Palavras
print(quantidade)
