idade = int(input('Digite sua idade: '))

if idade < 0 :
    print('Impossível!')
    print('Não precisa se alistar.')

elif idade < 18:
    print('Não precisa se alistar.')

elif idade > 18 and idade < 65:
    print('Não esqueça de votar na próxima eleição.')

elif idade > 65:
    print('Vá descansar.')
else:
    print('Eita!')