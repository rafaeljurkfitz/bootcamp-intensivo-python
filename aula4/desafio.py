import csv

def validar_nome(nome: str) -> bool:
    if len(nome) == 0:
        raise ValueError("O nome não pode estar vazio.")
    elif any(char.isdigit() for char in nome):
        raise ValueError("O nome não deve conter números.")
    else:
        return True

def validar_salario(salario: float) -> bool:
    if salario < 0:
        raise ValueError("Por favor, digite um valor positivo para o salário.")
    else:
        return True

def validar_bonus(bonus_recebido: float) -> bool:
    if bonus_recebido < 0:
        raise ValueError("Por favor, digite um valor positivo para o bônus.")
    else:
        return True
    
def validar_kpi_bonus_final(salario: float, bonus_recebido: float) -> float:
    bonus_final = bonus_recebido * 1.2
    kpi = (salario + bonus_final) / 1000
    return kpi, bonus_final

def salvar_dados(registros: dict) -> None:
    with open("registros.csv", mode="w") as arquivo:
        cabecalho = ["nome", "salario", "bonus_recebido", "bonus_final", "kpi"]
        escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)
        escritor.writeheader()
        escritor.writerow(registros)

def carregar_dados() -> None:
    with open("registros.csv", mode="r") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            print(linha)

def cadastrar(nome_valido: bool, salario_valido: bool, bonus_valido: bool) -> None:
    registros = {}
    
    while not nome_valido:
        try:
            nome: str = input("Digite seu nome: ")
            nome_valido = validar_nome(nome)
            print(f"{nome} é um nome válido.")
        except ValueError as e:
            print(e)

    while not salario_valido:
        try:
            salario: float = float(input("Digite o valor do seu salário: "))
            salario_valido = validar_salario(salario)
            print(f"O salario de {salario} é um valor de salario válido.")
        except ValueError as e:
            print(e)

    while not bonus_valido:
        try:
            bonus_recebido: float = float(input("Digite o valor do bônus recebido: "))
            bonus_valido = validar_bonus(bonus_recebido)
            print(f"O bonus de {bonus_recebido} é um valor de bonus válido.")
        except ValueError:
            print(e)

    kpi, bonus_final = validar_kpi_bonus_final(salario, bonus_recebido)
    
    registros = {
        "nome": nome,
        "salario": salario,
        "bonus_recebido": bonus_recebido,
        "bonus_final": bonus_final,
        "kpi": kpi
    }

    salvar_dados(registros)
    
    carregar_dados()


def main() -> None:
    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False
    
    cadastrar(nome_valido, salario_valido, bonus_valido)

    
if __name__ == "__main__":
    main()
        