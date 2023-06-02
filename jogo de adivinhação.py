# Jogo de Adivinhação
# Neste jogo, o jogador precisa adivinhar um número secreto entre 1 e 100.
# O jogador começa com 1000 pontos e perde 20 pontos a cada chute incorreto.
# A dificuldade do jogo é escolhida pelo jogador (fácil, médio ou difícil) e afeta a quantidade de pontos perdidos.
# O jogador pode sair do jogo a qualquer momento digitando 'X'.
# No final, o jogo exibe a pontuação obtida pelo jogador.

import random

pontos = 1000
secreto = random.randint(1, 100)
print("Bem-vindo ao jogo!")
print("Tente adivinhar o número de 1 a 100")
dificuldade = int(input("[1] Fácil\n[2] Médio \n[3] Difícil: "))

# Loop principal do jogo
while True:
    chute = input("Digite o seu chute\n[X] Para finalizar: ")
    
    if chute.upper() == 'X':  # Verifica se o jogador digitou 'X' para sair do jogo
        break
    
    if not chute.isdigit():  # Verifica se a entrada não é um número válido
        print("Chute inválido. Por favor, digite um número válido.")
        continue
    
    chute = int(chute)
    
    if secreto > chute:  # Verifica se o chute está abaixo do número secreto
        print("O chute foi menor\n")
        pontos -= 20 * dificuldade
    
    elif secreto < chute:  # Verifica se o chute está acima do número secreto
        print("O chute foi maior\n")
        pontos -= 20 * dificuldade
    
    elif chute == secreto:  # Verifica se o chute acertou o número secreto
        break

if chute == secreto:  # Verifica se o jogador acertou o número secreto
    print(f"Você acertou e seus pontos são {pontos}")
else:
    print("Você não fez nenhum ponto e finalizou o programa!")
