
from datetime import date

atual = date.today().year
menor = 0
maior = 0

for c in range(1,8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu '.format(c)))
    idade = atual - nascimento
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('Tivemos {} pessoas MAIORES DE IDADE'.format(maior))
print('Tivemos {} pessoas MENORES DE IDADE'.format(menor))
