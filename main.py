nome = input('Quem está utilizando? ').upper()
qtdRendas = int(input('Quantas Rendas você possui? ' ))
contaRendas = 0
total_renda = 0
while contaRendas < qtdRendas: 
    renda = float(input('Informe o Valor da Renda: '))
    total_renda = total_renda + renda
    contaRendas = contaRendas + 1

    
print('-----------------------------------------------') 
print(f'CONTROLADOR DE FINANÇAS DO {nome}')   
print(f'Olá {nome}, Vamos organizar suas finaças?')
print(f'Você Possui {qtdRendas} rendas.')
print(f'E o Seu Saldo total é: {total_renda}')
print(f'Informe agora as suas despesas.')

qtdDesp = int(input('Quantas despesas você possui? '))
contaDesp = 0
total_despesa = 0
while contaDesp < qtdDesp: 
    despesa = float(input('Informe o valor da despesa: '))
    total_despesa = total_despesa + despesa
    contaDesp = contaDesp + 1    
    

print(f'Você possui: {qtdDesp} despesas.')
print(f'Elas somadas tomam R${total_despesa:.2f} seu.')  
valorFinal = total_renda - total_despesa  
print(f'E o total final é: R${valorFinal:.2f}')
print('-----------------------------------------------') 


