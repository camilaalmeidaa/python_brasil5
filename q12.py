from random import shuffle

def embaralha_palavra(palavra):
    
    opcoes = list(palavra)
    
    shuffle(opcoes)
    opcoes = ''.join(opcoes)
    print(opcoes.lower())


