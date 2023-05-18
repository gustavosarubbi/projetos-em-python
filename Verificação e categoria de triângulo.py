# Programa: Verificação e categoria de triângulo
# Descrição: Este programa solicita ao usuário os comprimentos dos três lados de um triângulo.
#            Em seguida, verifica se os lados inseridos formam um triângulo e determina a categoria do triângulo.
#            As categorias possíveis são: equilátero (todos os lados iguais), isósceles (dois lados iguais) ou escaleno (todos os lados diferentes).

lado1 = float(input("Insira o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Insira o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Insira o comprimento do terceiro lado do triângulo: "))

# Verificar se os lados inseridos formam um triângulo
if lado1 >= lado2 + lado3 or lado2 >= lado1 + lado3 or lado3 >= lado1 + lado2:
    print("Os lados inseridos não formam um triângulo.")
# Verificar se o triângulo é equilátero
elif lado1 == lado2 and lado2 == lado3:
    print("O triângulo é equilátero.")
# Verificar se o triângulo é isósceles
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("O triângulo é isósceles.")
# Caso contrário, o triângulo é escaleno
else:
    print("O triângulo é escaleno.")
