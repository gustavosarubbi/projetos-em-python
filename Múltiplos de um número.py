# Programa: Múltiplos de um número
# Descrição: Este programa solicita ao usuário um número e o valor do múltiplo.
#            Em seguida, calcula e exibe os múltiplos do número fornecido até o múltiplo especificado.
#            Caso o usuário insira um valor de múltiplo negativo ou zero, o programa solicitará novamente um valor válido.

numero = int(input("Qual número desejado?\n"))

# Solicitação do valor do múltiplo até que um valor positivo seja fornecido
while True:
    multiplo = int(input("Até qual múltiplo você deseja?\n"))
    if multiplo <= 0:
        print("O valor do múltiplo deve ser positivo. Tente novamente.")
    else:
        break

# Cálculo e exibição dos múltiplos
for i in range(1, multiplo + 1):
    print(f"{i}x{numero}: {numero * i}\t", end="")
    if i % 10 == 0:
        print()

