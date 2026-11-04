from random import randint
from time import sleep

lista = []
jogos = int(input('Quantos jogos irão ser gerados?: '))

for j in range(jogos):
    dados = []
    for r in range(0,6):
        sorteado = randint(1,60)
        while sorteado in dados:
            sorteado = randint(1,60)
        dados.append(sorteado)
    lista.append(dados[:])
    dados.clear()

sleep(1)
print()
print(f'Sorteando {jogos} jogos...')
print()
sleep(1)


for j in range(jogos):
    print(f'Resultado jogo {j+1}: {sorted(lista[j])}')
    sleep(1)
print('Boa sorte ! :)')