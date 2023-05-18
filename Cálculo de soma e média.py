# Programa: Cálculo de soma e média
# Descrição: Este programa solicita ao usuário que digite números, realiza a soma desses números e calcula a média.
#            O programa encerra quando o usuário digita 'X' ou 'x'.

soma = 0
quantidade = 0

# Loop principal do programa
while True:
    entrada = input("Digite um número:\n[X] para finalizar o programa:\n").upper()
    
    # Verifica se o usuário deseja encerrar o programa
    if entrada == 'X':
        break

    # Converte a entrada para um número float
    numero = float(entrada)
    soma += numero
    quantidade += 1

# Verifica se algum número foi inserido
if quantidade == 0:
    print("Nenhum número foi inserido!")
else:
    # Calcula a média e exibe o resultado
    print("A soma dos números é {:.2f} e a média é {:.2f}".format(soma, soma / quantidade))
