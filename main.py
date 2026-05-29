from rendas import calcular_rendas
from despesas import calcular_despesas
from relatorio import calcular_saldo

nome = input('Quem está utilizando? ').upper()

renda = calcular_rendas()
despesas = calcular_despesas()

saldo_total = calcular_saldo(renda, despesas)



print(f'''------------------------------------------------
      CONTROLADOR DE FINANÇAS DO {nome}
------------------------------------------------''') 
print(f'Renda: {renda}')
print(f'Valor Total: {despesas} ')
print(f'Valor Total:  {saldo_total} ')



