def cores(c='limpa'):
    if c == 'limpa':
        c = '\033[m'
        return c
    if c == 'azul':
        c = '\033[34m'
        return c
    if c == 'verde':
        c = '\033[32m'
        return c
    if c == 'vermelho':
        c = '\033[31m'
        return c
    if c == 'amarelo':
        c = '\033[33m'
        return c
    if c == 'azule':
        c = '\033[36m'
        return c
