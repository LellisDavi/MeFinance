def calcular_despesas():
    qtd_despesas = int(input('Quantas despesas você possui? '))
    
    total_despesas = 0

    for i in range(qtd_despesas):
        despesa = float(input('Despesa: '))
        total_despesas += despesa

    return total_despesas


