def validainteiro(nint):
    while True:
        try:
            nint = int(input(nint))
            break
        except ValueError:
            print('\033[1;31m> ERRO! Digite uma idade válida.\033[m')
    return nint


def validapalavra(nome):
    global n, numeros
    numeros = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.strip()
    while True:
        try:
            n = str(input(nome)).strip()
            separa = n.split()
            junta = ''.join(separa)
            for v in junta.strip():
                if v not in numeros:
                    n = int('r')
            if n.strip() == '':
                n = int('d')
            break
        except ValueError:
            print('\033[1;31m> ERRO! Digite apenas letras.\033[m')
    return n


def exibearquivo(arq):
    try:
        abriarq = open(arq, 'rt')
    except FileNotFoundError:
        abriarq = open(arq, 'wt+')
    print(abriarq.read())


def existe_dados_em_arquivo(arq):
    valor = False
    abriarq = open(arq, 'rt')
    if abriarq.read():
        valor = True
    return valor


def cadastrar(arq, nome, idade):
    c = open(arq, 'at')
    if existe_dados_em_arquivo(arq):
        c.write(f'\n{nome:<40}{idade:<} anos')
    else:
        c.write(f'{nome:<40}{idade:<} anos')


def verificacadastrado(arq, nome):
    global valor
    nenhum_cadastro = ''
    nomes_cadastrados = []
    abriarq = open(arq, 'rt')
    if not abriarq.read():
        nenhum_cadastro = 'nada'
    abriarq = open(arq, 'rt')
    for dados in abriarq:
        poe_nomes_numalista = dados.split()
        ulti_posi, penulti_posi = poe_nomes_numalista[-1], poe_nomes_numalista[-2]
        poe_nomes_numalista.remove(ulti_posi), poe_nomes_numalista.remove(penulti_posi)
        nomes_cadastrados.append(' '.join(poe_nomes_numalista))
    if nenhum_cadastro == 'nada':
        valor = True
    else:
        if nome not in nomes_cadastrados:
            valor = True
        else:
            valor = False
    return valor
