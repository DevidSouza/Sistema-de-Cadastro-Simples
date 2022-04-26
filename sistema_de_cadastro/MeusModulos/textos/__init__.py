def titulo(tit):
    print('\033[1m', end='')
    print(50 * '~')
    print(f'{tit:^50}')
    print(50 * '~', end='')
    print('\033[m')


def menu(* menu):
    c = 1
    print('\033[1;36m', end='')
    print(50*'~')
    print('MENU PRINCIPAL'.center(50))
    print(50 * '~')
    print('\033[m', end='')
    for n in menu:
        print(f'\033[1;36m{c} - \033[1;34m{n}\033[m')
        c += 1
    while True:
        opc = input('\033[1;36mDigite sua opção: ')
        if opc == '1' or opc == '2' or opc == '3':
            break
        print('\033[1;31mERRO! Digite uma opção válida.\033[m')
    return opc
