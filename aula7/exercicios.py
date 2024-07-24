"""
1.Calcular Média de Valores em uma Lista

2.Filtrar Dados Acima de um Limite

3.Contar Valores Únicos em uma Lista

4.Converter Celsius para Fahrenheit em uma Lista

5.Calcular Desvio Padrão de uma Lista

6.Encontrar Valores Ausentes em uma Sequência
"""

from typing import List


# Exercicio 1
def media_valores(lista: List[float]) -> float:
    return sum(lista) / len(lista)

# Exercicio 2
def filtrar_dados(lista: List[float], limite: float) -> List[float]:
    return [valor for valor in lista if valor > limite]

# Exercicio 3
def contar_valores_unicos(lista: List[float]) -> int:
    return len(set(lista))

# Exercicio 4
def celsius_para_fahrenheit(lista: List[float]) -> List[float]:
    return [valor * 1.8 + 32 for valor in lista]

# Exercicio 5 - Extra
def variancia(media: float, lista: List[float] ) -> float:
    return sum((valor - media) ** 2 for valor in lista) / len(lista)

# Exercicio 5
def desvio_padrao(lista: List[float]) -> float:
    media = media_valores(lista)
    return (variancia(media, lista)) ** 0.5

# Exercicio 6
def valores_ausentes(sequencia: List[int]) -> List[int]:
    return [valor for valor in range(1, max(sequencia) + 1) if valor not in sequencia]


################################### GABARITO ###################################

from typing import List

# Exercicio 1
def calcular_media(valores: List[float]) -> float:
    return sum(valores) / len(valores)

# Exercicio 2
def filtrar_acima_de(valores: List[float], limite: float) -> List[float]:
    resultado = []
    for valor in valores:
        if valor > limite:
            resultado.append(valor)
    return resultado

# Exercicio 3
def contar_valores_unicos(lista: List[int]) -> int:
    return len(set(lista))

# Exercicio 4
def celsius_para_fahrenheit(temperaturas_celsius: List[float]) -> List[float]:
    return [(9/5) * temp + 32 for temp in temperaturas_celsius]

# Exercicio 5
def calcular_desvio_padrao(valores: List[float]) -> float:
    media = sum(valores) / len(valores)
    variancia = sum((x - media) ** 2 for x in valores) / len(valores)
    return variancia ** 0.5

# Exercicio 6
def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    completo = set(range(min(sequencia), max(sequencia) + 1))
    return list(completo - set(sequencia))
