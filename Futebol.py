import webbrowser
times = ('São Paulo', 'Palmeiras', 'Corinthians', 'Flamengo',
         'Santos', 'Fluminense', 'Vasco', 'Botafogo')
print('_'*20)
print(f'Os melhores times Rio/SP são: {times}.')
print('_'*20)
print(f'Os times Rios/SP em ordem alfabética: {sorted(times)}.')
print('_'*20)
print(f'O São Paulo está na {times.index("São Paulo")+1} posição')
print('_'*20)
print(f'O São Paulo Eliminou {times[1:4]} para ganhar uma competição :)')
print('_'*20)
print(f'Esses times não ganham nada a um tempo -> {times[-4:]}.')
print('_'*20)
copa = int(input('''Precisamos voltar ao assunto da competição que eu falei. 
Digite 1 para ver a competição que o São Paulo FC ganhou:  '''))
if copa == 1:
    url = 'https://www.instagram.com/p/Cx8yGdtuZNw/'
    webbrowser.open(url)
else:
    print('Seu chato. O São Paulo é campeão da Copa do Brasil. É CAMPEÃO!!!')
