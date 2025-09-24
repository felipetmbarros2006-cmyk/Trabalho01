def contar_palavra(frase, palavra):
    frase_minuscula = frase.lower()
    palavra_minuscula = palavra.lower()
    palavras_frase = frase_minuscula.split()
    return palavras_frase.count(palavra_minuscula)