# Programa: Análise de Dados Pessoais
# Descrição: Este programa solicita ao usuário a idade e o estado civil de várias pessoas e realiza análises estatísticas
#            com base nos dados fornecidos, incluindo a quantidade de pessoas casadas, solteiras, viúvas, a média de idade
#            das pessoas viúvas e a porcentagem de pessoas desquitadas ou separadas em relação ao total de pessoas.

casados = 0
solteiros = 0
viuvos = 0
somaIdadeViuvos = 0
totalPessoas = 0

# Loop principal do programa para capturar os dados das pessoas
while True:
    idade = int(input("Digite a idade da pessoa\nNúmero negativo para finalizar\n"))

    if idade < 0:
        break

    estadoCivil = input("Digite o estado civil da pessoa (C-casado, S-solteiro, V-viúvo, D-desquitado ou separado)\n").upper()

    totalPessoas += 1

    if estadoCivil == 'C':
        casados += 1
    elif estadoCivil == 'S':
        solteiros += 1
    elif estadoCivil == 'V':
        viuvos += 1
        somaIdadeViuvos += idade
    elif estadoCivil == 'D':
        totalPessoas -= 1
    else:
        print("Estado civil inválido.")
        totalPessoas -= 1

    print()

# Verificar se há pessoas para análise
if totalPessoas > 0:
    # Calcular a média das idades das pessoas viúvas
    mediaIdadeViuvos = somaIdadeViuvos / viuvos if viuvos > 0 else 0
    # Calcular a porcentagem de pessoas desquitadas ou separadas em relação ao total de pessoas
    porcentagemDesquitados = (totalPessoas - casados - solteiros - viuvos) / totalPessoas * 100

    # Exibir os resultados da análise
    print("Quantidade de pessoas casadas:", casados)
    print("Quantidade de pessoas solteiras:", solteiros)
    print("Média das idades das pessoas viúvas: {:.2f}".format(mediaIdadeViuvos))
    print("Porcentagem de pessoas desquitadas ou separadas: {:.2f}%".format(porcentagemDesquitados))
else:
    print("Nenhuma pessoa analisada.")
