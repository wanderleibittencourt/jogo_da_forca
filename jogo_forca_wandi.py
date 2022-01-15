

import os
clear = lambda: os.system('cls')
from time import sleep

braçoe = ' '
braçod = ' '
cabeça = ' '
corpo = ' '
pernae = ' '
pernad = ' '
erro = 0
while True:
  chutes = ''

  while True:
    palavra = str(input('Palavra: ')).strip()
    if not palavra.isnumeric() and palavra.isalpha():
      break
    else:
      print(f'ERRO:"{palavra}" não é válido. Digite uma palavra apenas com letras')

  palavra = palavra.upper()
  dica = str(input('Dica: ')).strip().upper()
  if dica == palavra:
    print('A dica não pode ser a resposta!')
   
  else:
    certo = '-' * len(palavra)
    break

while True:
  clear()
  print('\/\/\/Jogo da forca\/\/\/')
  print(f'Dica: {dica}\n')
  print(f'Letras usadas: {chutes}\n')
  print(f''' {cabeça}
{braçoe}{corpo}{braçod}
{pernae} {pernad}''')
  print(certo, ' >', len(certo),'letras')
  if certo == palavra:
    print('Você ganhou!')
    print('Fim de jogo.')
    sleep(3)
    break

  while True:
    chute = str(input('Chute uma letra!\n')).strip()
    if len(chute) == 1 and chute.isalpha():
      break
    else:
      print(f'ERRO!:"{chute}" não é válido. Digite apenas uma letra')

  chute = chute.upper()
  if chute in chutes:
    print('Você já tentou essa letra')
    sleep(1.5)
    continue
  chutes = chutes + chute + ' - '
  if chute not in palavra:
    erro += 1
  else:
    for n,l in enumerate(palavra):
      if chute == l:
        certo = certo[:n] + l + certo[n+1:]
  
  if erro >= 5:
    braçoe = '-'
  if erro >= 6:
    braçod = '-'
  if erro >= 1:
    cabeça = 'O'
  if erro >= 2:
    corpo = '|'
  if erro >= 3:
    pernae = '/'
  if erro >= 4:
    pernad = "\ "
    
  if erro == 7:
    print('ENFORCADO!!!')
    print('FIM DE JOGO.')
    sleep(3)
    break