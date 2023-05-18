# Programa: Organizar 3 variáveis
# Descrição: Este programa recebe três números do usuário e os ordena em ordem crescente ou decrescente de acordo com a escolha do usuário.

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
opcao = int(input("[1] Crescente  [2] Decrescente\nEscolha a opção de ordenação: "))

# Ordenar os números em ordem crescente
if numero1 > numero2:
    numero1, numero2 = numero2, numero1
if numero2 > numero3:
    numero2, numero3 = numero3, numero2
if numero1 > numero2:
    numero1, numero2 = numero2, numero1

# Exibir os números em ordem crescente ou decrescente, de acordo com a opção escolhida
if opcao == 1:
    print("Os valores em ordem crescente: {:.2f} {:.2f} {:.2f}".format(numero1, numero2, numero3))
elif opcao == 2:
    print("Os valores em ordem decrescente: {:.2f} {:.2f} {:.2f}".format(numero3, numero2, numero1))
else:
    print("Opção inválida.")
