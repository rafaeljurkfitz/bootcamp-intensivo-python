# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas

nome_valido = False
salario_valido = False
bonus_valido = False


while not nome_valido:
    try:
        nome = input("Digite seu nome: ")
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            nome_valido = True
            print(f"{nome} é um nome válido.")
    except ValueError as e:
        print(e)

while not salario_valido:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            raise ValueError("Por favor, digite um valor positivo para o salário.")
        salario_valido = True
        print(f"O salario de {salario} é um valor de salario válido.")
    except ValueError as e:
        print(e)

while not bonus_valido:
    try:
        bonus_recebido = float(input("Digite o valor do bônus recebido: "))
        if bonus_recebido < 0:
            raise ValueError("Por favor, digite um valor positivo para o bônus.")
        bonus_valido = True
        print(f"O bonus de {bonus_recebido} é um valor de bonus válido.")
    except ValueError:
        print(e)

bonus_final = bonus_recebido * 1.2
kpi = (salario + bonus_final) / 1000

print(f"Seu KPI é: {kpi:.2f}")
print(f"Olá, {nome}! Seu salário é de R${salario:.2f} e você recebeu um bônus final de R${bonus_final:.2f}.")
