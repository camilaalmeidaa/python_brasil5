import random

def jogar_craps():
    
    return random.randint(2, 12)


entrada = ""
jogada = 0
ponto = 0

print("Digite sair para encerrar o jogo.\nAperte <enter> para rolar os dados: ")

while (entrada != "sair"):
    
    jogada += 1
    
    print("Jogada",jogada)
    
    entrada = input("Esperando o enter...")

    if entrada == "sair":
        
        print("Saindo do jogo...")
        
    else:
        
        if (jogada > 1):
            
            print("Sua pontuação é:",ponto)
            
        valor = jogar_craps()
        
        print("O valor do dado é:",valor)
        
        if(jogada == 1):
            
            if (valor == 7) or (valor == 11):
                
                print("Você tirou um natural e ganhou! :)")
                exit()
                
            elif (valor == 2) or (valor == 3) or (valor == 12):
                
                print("Você tirou um craps e perdeu... :(") 
                exit()
                
            else:
                ponto = valor
                
        else:
            
            if (valor == 7):
                
                print("Você tirou um 7 antes de repetir seu ponto, você perdeu... :(")
                exit()
                
            elif (ponto == valor):
                
                print("Você conseguiu repetir seu ponto e ganhou! :)")
                exit()