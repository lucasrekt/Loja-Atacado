print('Bem vindo a Loja do Lucas')

# Realizando um pedido de valor do produto e a quantidade. Try usado para conferir se é um número.

try:
    # variável "valor" solicitando que o usuário digite um número do valor da peça.
    valor = float(input('Digite o valor do produto: '))
    # variável "quant" solicitando a quantidade que o usuário deseja levar da peça.
    quant = int(input('Digite a quantidade que irá levar: '))
    # variável "qv" sendo atribuido a equação entre o valor da peça vezes a quantidade para o valor final.
    qv = valor * quant

# Condição indicando se a quantidade for menor ou igual a 9, não realizar nenhum desconto.
    if quant <= 9:
        # mostra na tela que a quantidade não se aplica a desconto.
        print('A quantidade de peças não se aplica a desconto.')
        # mostra na tela o valor final.
        print('O valor final é R${:.2f}'.format(qv))

# Condição para que caso a quantidade seja maior ou igual a 10 e menor ou igual a 99, seja aplicado um desconto de 5%.
    elif 10 <= quant <= 99:
        # Calculo de desconto com 5%.
        vf = qv - (qv * (5 / 100))
        # mostra na tela o valor sem desconto.
        print('O valor sem desconto é R${:.2f}'.format(qv))
        # mostra na tela o valor com o desconto de 5% aplicado.
        print('O valor com desconto fica R${:.2f}  (desconto de 5%)'.format(vf))
# Condição para caso a quantidade seja maior ou igual a 100 e menor ou igual a 999, seja aplicado um desconto de 10%.
    elif 100 <= quant <= 999:
        # Calculo de desconto com 10%.
        vf = qv - (qv * (10 / 100))
        # mostra na tela o valor sem desconto.
        print('O valor sem desconto é R${:.2f}'.format(qv))
        # mostra na tela o valor com o desconto de 10% aplicado.
        print('O valor com desconto fica R${:.2f}  (desconto de 10%)'.format(vf))
    elif quant >= 1000:
        # Calculo de desconto com 15%.
        vf = qv - (qv * (15 / 100))
        # mostra na tela o valor sem desconto.
        print('O valor sem desconto é R${:.2f}'.format(qv))
        # mostra na tela o valor com o desconto de 15% aplicado.
        print('O valor com desconto fica R${:.2f}  (desconto de 15%)'.format(vf))

# Exceções para caso não seja digitado um número e encerre o programa.
# Exceção "ValueError" indicando que o que foi digitado não é um valor.
# Exceção "TypeError" para caso o que foi digitado não seja um float.
except(ValueError, TypeError):
    print('Esse não é um número válido.\n'
          'Encerrando o programa...')
