# Q6 - Conversor de Moedas
# Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
# real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) 
# o default deve ser real_para_dolar <- padrão

from converter import real_para_dolar, dolar_para_real

valor = float(input("Digite o valor: ") or 1)
cotacao = float(input("Digite a cotação do dólar: "))
tipo = int(input("Digite o tipo de conversão [1] real para dolar ou [2] dolar para real: ")) 

match tipo:
    case 1:
        resultado = real_para_dolar(valor, cotacao)
        print(f"\n{valor:.2f} reais equivalem a {resultado:.2f} dólares.")
    case 2:
        resultado = dolar_para_real(valor, cotacao)
        print(f"\n{valor:.2f} dólares equivalem a {resultado:.2f} reais.")
    case _:
        print("Seleção não válida, utilizando conversão (default), real para dolar! ")
        resultado = real_para_dolar(valor, cotacao)
        print(f"\n{valor:.2f} reais equivalem a {resultado:.2f} dólares.")

