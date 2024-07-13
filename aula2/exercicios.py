#### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
soma = valor1 + valor2
print(f"A soma dos valores é: {soma}")
# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
resto_divisao = valor1 % 5
print(f"O resto da divisão é: {resto_divisao}")
# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
multiplicacao = valor1 * valor2
print(f"A multiplicação dos valores é: {multiplicacao}")
# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
divisao = valor1 // valor2
print(f"A divisão inteira dos valores é: {divisao}")
# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
quadrado = valor1 ** 2
print(f"O quadrado do valor é: {quadrado}")

#### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
adição = valor1 + valor2
print(f"A adição dos valores é: {adição}")
# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
media = (valor1 + valor2) / 2
print(f"A média dos valores é: {media}")
# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite o valor da base: "))
expoente = float(input("Digite o valor de expoente: "))
potencia = base ** expoente
print(f"A potência dos valores é: {potencia}")
# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"A temperatura em Fahrenheit é: {fahrenheit}")
# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
import math
raio = float(input("Digite o valor do raio: "))
area = math.pi * raio ** 2
print(f"A área do círculo é: {area}")

#### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
string = input("Digite uma string: ")
string_maiuscula = string.upper()
print(f"A string em maiúscula é: {string_maiuscula}")
# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Digite o seu nome completo: ")
nome_minusculo = nome.lower()
print(f"O nome em minúsculo é: {nome_minusculo}")
# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip(" ")
print(f"A frase sem espaços em branco é: {frase_sem_espacos}")
# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data = input("Digite uma data no formato 'dd/mm/aaaa': ")
dia, mes, ano = data.split("/")
print(f"Dia: {dia}")
print(f"Mês: {mes}")
print(f"Ano: {ano}")
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")
concatenacao = string1 + string2
print(f"A concatenação das strings é: {concatenacao}")

#### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
expressao1 = True
expressao2 = False
resultado = expressao1 and expressao2
print(f"O resultado da operação AND é: {resultado}")
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1 = False
valor2 = True
resultado = valor1 or valor2
print(f"O resultado da operação OR é: {resultado}")
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
valor = True
valor_invertido = not valor
print(f"O valor invertido é: {valor_invertido}")
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
numero1 = 10
numero2 = 10
resultado = numero1 == numero2
print(f"Os números são iguais? {resultado}")
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
resultado2 = numero1 != numero2
print(f"Os números são diferentes? {resultado2}")

#### try-except e if

# 21: Conversor de Temperatura
try:
    celsius = float(input("Digite a temperatura em Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C em Fahrenheit é: {fahrenheit}")
except ValueError:
    print("Por favor, digite um valor numérico.")
# 22: Verificador de Palíndromo
palavra = input("Digite uma palavra: ")
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print("A palavra é um palíndromo.")
else:
    print("A palavra não é um palíndromo.")
# 23: Calculadora Simples
try:
    valor = float(input("Digite um valor: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    valor2 = float(input("Digite outro valor: "))
    if operacao == "+":
        resultado = valor + valor2
    elif operacao == "-":
        resultado = valor - valor2
    elif operacao == "*":
        resultado = valor * valor2
    elif operacao == "/":
        resultado = valor / valor2
    else:
        print("Operação inválida.")
    print(f"O resultado da operação é: {resultado}")
except ValueError:
    print("Por favor, digite valores numéricos.")
# 24: Classificador de Números
try:
    numero = int(input("Digite um número: "))
    if numero > 0:
        print("Positivo")
    elif numero < 0:
        print("Negativo")
    else:
        print("Zero")
    if numero % 2 == 0:
        print("Par")
    else:
        print("Ímpar")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
# 25: Conversão de Tipo com Validação
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")