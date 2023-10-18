#Criar um sistema de informação que receba o dia e o mês de nascimento de uma pessoa e informe o signo (com base na tabela anexa).

print('\n\t\t\t -- Qual é o seu signo -- \t\t\t')

dia = int(input('Informe o dia em que nasceu: '))
mes = int(input('Informe o mês em que nasceu: '))

if mes == 1:
    if dia <= 20:
        print('Seu signo é Capricórnio.')
    else:
        print('Seu signo é Aquário.')

elif mes == 2:
    if dia <= 18:
        print('Seu signo é Aquário.')
    else:
        print('Seu signo é Peixes.')

elif mes == 3:
    if dia <= 19:
        print('Seu signo é Peixes.')
    else:
        print('Seu signo é Áries.')

elif mes == 4:
    if dia <= 20:
        print('Seu signo é Áries.')
    else:
        print('Seu signo é Touro.')

elif mes == 5:
    if dia <= 20:
        print('Seu signo é Touro.')
    else:
        print('Seu signo é Gêmeos.')

elif mes == 6:
    if dia <= 20:
        print('Seu signo é Gêmeos.')
    else:
        print('Seu signo é Câncer.')

elif mes == 7:
    if dia <= 21:
        print('Seu signo é Câncer.')
    else:
        print('Seu signo é Leão.')

elif mes == 8:
    if dia <= 22:
        print('Seu signo é Leão.')
    else:
        print('Seu signo é Virgem.')

elif mes == 9:
    if dia <= 22:
        print('Seu signo é Virgem.')
    else:
        print('Seu signo é Libra.')

elif mes == 10:
    if dia >= 22:
        print('Seu signo é Libra.')
    else:
        print('Seu signo é Escorpião.')

elif mes == 11:
    if dia <= 21:
        print('Seu signo é Escorpião.')
    else:
        print('Seu signo é Sagitário.')

elif mes == 12:
    if dia >= 21:
        print('Seu signo é Sagitário.')
    else:
        print('Seu signo é Capricórnio.')


