from MeusModulos import textos, dados
from time import sleep
arq = 'dados_cadastrados.txt'
print('\033[1;3;36m>> SISTEMA DE CADASTRO\033[m\n')
try:
    # MENU PRINCIPAL:
    while True:
        sleep(1)
        opcao = textos.menu('Pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema')
        sleep(0.5)
        # OPÇÃO 01 (exibe a opção digitada)
        if opcao == '1':
            sleep(0.8), textos.titulo('PESSOAS CADASTRADAS')
            print('\033[34m', end=''), dados.exibearquivo(arq), print('\033[m', end='')

        # OPÇÃO 02 (captura nome e idade):
        elif opcao == '2':
            textos.titulo('NOVO CADASTRO')
            while True:
                nome = dados.validapalavra('\033[1;34m- Nome: ').strip().title()
                # VERIFICA SE NOME JÁ ESTÁ CADASTRADO:
                if dados.verificacadastrado(arq, nome):
                    break
                print('\033[1;31m> Nome já registrado no banco de dados!\033[m')
            idade = dados.validainteiro('\033[1;34m- Idade: ')
            # SALVA DADOS NO ARQUIVO:
            dados.cadastrar(arq, nome, idade)
            for p in range(0, 3):
                print('.', end=''), sleep(1)
            print('\n\033[1;32m> Dados registrados com sucesso!\033[m')
        # OPÇÃO 3 (sai do sistema):
        elif opcao == '3':
            break

    print(f'\n\033[1;33mENCERRANDO PROGRAMA', end='')
    sleep(1)
    for p in range(0, 3):
        print('.', end=''), sleep(1)
    print('\n>>> ATÉ MAIS <<<')
except KeyboardInterrupt:
    print('\n\033[1;33mPROGRAMA INTERROMPIDO PELO USUÁRIO.\033[m')
