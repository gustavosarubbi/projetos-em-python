# Programa: Encontrar o maior e o menor valor de uma sequência de números
# Descrição: Este programa solicita ao usuário que digite números e armazena o maior e o menor valor encontrados. O usuário pode encerrar a sequência digitando 'x' (maiúsculo ou minúsculo).

import sys

big = 0
small = sys.maxsize  # Variáveis para armazenar o maior e o menor valor
numb = ''  # String para armazenar a entrada do usuário

while True:
    numb = input("Digite números\n[x] para sair\n")
    
    if numb.lower() == 'x':
        break
    
    n = int(numb)

    if n > big:
        big = n
    if n < small:
        small = n

print("O maior da sequência é {} e o menor valor é {}".format(big, small))
