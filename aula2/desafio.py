### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome
try:
    nome = input("Digite seu nome: ")
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        pass
except ValueError as e:
    print(e)

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario = float(input("Digite o valor do seu salário: "))
    if salario < 0:
        raise ValueError("Por favor, digite um valor positivo para o salário.")
except ValueError as e:
    print(e)

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_recebido = float(input("Digite o valor do bônus recebido: "))
    if bonus_recebido < 0:
        raise ValueError("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print(e)

# 4) Calcule o valor do bônus final
bonus_final = bonus_recebido * 1.2
kpi = (salario + bonus_final) / 1000

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"Seu KPI é: {kpi:.2f}")
print(f"Olá, {nome}! Seu salário é de R${salario:.2f} e você recebeu um bônus final de R${bonus_final:.2f}.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?