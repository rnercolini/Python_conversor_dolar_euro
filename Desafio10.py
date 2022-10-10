# Converte valor em dólar e euro
n = float(input('Digite o valor para converter em dólar e euro: R$'))
d = n / 5.21
e = n / 5.25
print('O valor de R${0:.2f} é igual a:\nUS${1:.2f}\n€{2:.2f}'.format(n, d, e))
